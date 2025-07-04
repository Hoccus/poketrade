from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Trade, TradeItem
from collection.models import CollectionItem
from django.contrib.auth.models import User

@login_required
def trade_list(request):
    # Get all trades where user is involved
    incoming_trades = Trade.objects.filter(recipient=request.user, status='pending')
    outgoing_trades = Trade.objects.filter(initiator=request.user)
    
    return render(request, 'trade/index.html', {
        'incoming_trades': incoming_trades,
        'outgoing_trades': outgoing_trades
    })

@login_required
def initiate_trade(request, user_id):
    recipient = get_object_or_404(User, id=user_id)
    if recipient == request.user:
        messages.error(request, "You cannot trade with yourself!")
        return redirect('trade.list')
    
    # Get user's collection items that are available for trade
    user_items = CollectionItem.objects.filter(user=request.user, status='collection')
    recipient_items = CollectionItem.objects.filter(user=recipient, status='collection')
    
    return render(request, 'trade/create.html', {
        'recipient': recipient,
        'user_items': user_items,
        'recipient_items': recipient_items
    })

@login_required
def create_trade(request):
    if request.method == 'POST':
        recipient_id = request.POST.get('recipient_id')
        offered_items = request.POST.getlist('offered_items')
        requested_items = request.POST.getlist('requested_items')
        
        if not offered_items or not requested_items:
            messages.error(request, "Please select at least one Pokémon from each side!")
            return redirect('trade.initiate', user_id=recipient_id)
        
        recipient = get_object_or_404(User, id=recipient_id)
        
        # Create new trade
        trade = Trade.objects.create(
            initiator=request.user,
            recipient=recipient,
            status='pending'
        )
        
        # Add offered items
        for item_id in offered_items:
            item = get_object_or_404(CollectionItem, id=item_id, user=request.user)
            item.status = 'pending'
            item.save()
            TradeItem.objects.create(
                trade=trade,
                item=item,
                recipient=recipient
            )
        
        # Add requested items
        for item_id in requested_items:
            item = get_object_or_404(CollectionItem, id=item_id, user=recipient)
            item.status = 'pending'
            item.save()
            TradeItem.objects.create(
                trade=trade,
                item=item,
                recipient=request.user
            )
        
        messages.success(request, "Trade offer sent successfully!")
        return redirect('trade.list')
    
    return redirect('trade.list')

@login_required
def cancel_trade(request, id):
    trade = get_object_or_404(Trade, id=id)

    for trade_item in trade.tradeitem_set.all():
        item = trade_item.item
        if item.status == 'pending':
            item.status = 'collection'
            item.save()

    trade.delete()

    messages.success(request, "Trade has been canceled and Pokémon returned to collection.")
    return redirect('trade.list')

@login_required
def edit_trade(request, id):
    trade = get_object_or_404(Trade, id=id, initiator=request.user)

    if trade.status != 'pending':
        messages.error(request, "Only pending trades can be edited.")
        return redirect('trade.list')

    if request.method == 'POST':
        old_offered_items = list(trade.tradeitem_set.filter(recipient=trade.recipient))
        old_requested_items = list(trade.tradeitem_set.filter(recipient=request.user))

        trade.tradeitem_set.all().delete()

        offered_items = request.POST.getlist('offered_items')
        requested_items = request.POST.getlist('requested_items')

        if not offered_items or not requested_items:
            messages.error(request, "Please select at least one Pokémon from each side!")
            return redirect('trade.edit_trade', id=trade.id)

        for item_id in offered_items:
            item = get_object_or_404(CollectionItem, id=item_id, user=request.user)
            item.status = 'pending'
            item.save()
            TradeItem.objects.create(
                trade=trade,
                item=item,
                recipient=trade.recipient
            )

        for item_id in requested_items:
            item = get_object_or_404(CollectionItem, id=item_id, user=trade.recipient)
            item.status = 'pending'
            item.save()
            TradeItem.objects.create(
                trade=trade,
                item=item,
                recipient=request.user
            )

        for item in old_offered_items:
            if str(item.item.id) not in offered_items:
                item.item.status = 'collection'
                item.item.save()

        for item in old_requested_items:
            if str(item.item.id) not in requested_items:
                item.item.status = 'collection'
                item.item.save()

        messages.success(request, "Trade updated successfully!")
        return redirect('trade.list')

    from django.db.models import Q

    user_items = CollectionItem.objects.filter(
        Q(user=request.user) & (Q(status='collection') | Q(id__in=trade.tradeitem_set.values_list('item_id', flat=True)))
    )

    recipient_items = CollectionItem.objects.filter(
        Q(user=trade.recipient) & (Q(status='collection') | Q(id__in=trade.tradeitem_set.values_list('item_id', flat=True)))
    )

    offered_item_ids = trade.tradeitem_set.filter(recipient=trade.recipient).values_list('item_id', flat=True)
    requested_item_ids = trade.tradeitem_set.filter(recipient=request.user).values_list('item_id', flat=True)

    return render(request, 'trade/edit.html', {
        'trade': trade,
        'user_items': user_items,
        'recipient_items': recipient_items,
        'offered_item_ids': offered_item_ids,
        'requested_item_ids': requested_item_ids,
    })


@login_required
def accept_trade(request, trade_id):
    trade = get_object_or_404(Trade, id=trade_id, recipient=request.user, status='pending')
    trade_items = TradeItem.objects.filter(trade=trade)
    
    # Process the trade
    for trade_item in trade_items:
        item = trade_item.item
        # Update ownership
        item.user = trade_item.recipient
        item.status = 'collection'
        item.save()
    
    trade.status = 'completed'
    trade.save()
    
    messages.success(request, "Trade completed successfully!")
    return redirect('trade.list')

@login_required
def reject_trade(request, trade_id):
    trade = get_object_or_404(Trade, id=trade_id, recipient=request.user, status='pending')
    
    # Return items to collection
    trade_items = TradeItem.objects.filter(trade=trade)
    for trade_item in trade_items:
        item = trade_item.item
        item.status = 'collection'
        item.save()
    
    trade.status = 'rejected'
    trade.save()
    
    messages.info(request, "Trade offer rejected")
    return redirect('trade.list')

@login_required
def users_list(request):

    # Get all users except current user
    users = User.objects.exclude(id=request.user.id)

    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        users = users.filter(username__icontains=search_query)

    return render(request, 'trade/users_list.html', {
        'users': users,
        'search_query': search_query,
    })