#  ___ __ ._`.*.'_._ ____ רףאל
#  . +  * .\   o.* `.`. +.  א .
# *  .ת' '  \^/|  `. * .  * `
#           \V/ . +
#  יהוה     /_\  .`.
# ======== _/W\_ =אדני:By: Two.0:.*
from django.urls import path
import blockchain.views

urlpatterns = [
    path('', blockchain.views.index, name='blockchain'),
    path('hash', blockchain.views.sign_Transaction, name="sign_Transaction"),
    # path('chain', blockchain.views.get_chain, name='get_chain'),
    # path('new_transaction', blockchain.views.new_transaction, name='new_transaction'),
    # path('mine', blockchain.views.mine_unconfirmed_transactions, name='mine'),
    # path('register_node', blockchain.views.register_new_peers, name='register_node'),
    # path('register_with', blockchain.views.register_with_existing_node, name='register_with'),
    # path('add_block', blockchain.views.verify_and_add_block, name='add_block'),
    # path('pending_tx', blockchain.views.get_pending_tx, name='pending_tx'),
    # path('submit', blockchain.views.submit_data, name='submit'),
    ]
