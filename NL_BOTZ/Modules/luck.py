# code added by @Jack_Network
# use with proper credits


from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from NL_BOTZ.helper_functions.cust_p_filters import f_onw_fliter

# LUCK------------ https://telegram.me/Jack_Network ------------ #

# EMOJI CONSTANTS
TRY_YOUR_LUCK = "🎰"
# EMOJI CONSTANTS

@Client.on_message(
    filters.command(["luck", "cownd"])
)
async def luck_cownd(client, message):
    """ /luck an @Jack_Network """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=TRY_YOUR_LUCK,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )
