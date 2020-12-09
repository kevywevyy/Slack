from server.general import AccessError, ValueError, decode_token, user_is_owner, valid_channel_id, id_to_user, id_to_channel, authorise_token

'''
ValueError - When user with user id u_id is not an owner of the channel
AccessError - AccessError when the authorised user is not an owner of the slackr, or an owner of this channel
'''

@authorise_token
def channel_removeowner(token, channel_id, u_id):
    # channel_id does not exist 
    if not valid_channel_id(channel_id):
        raise ValueError(description="Channel does not exist")
    else: 
        owner_user = id_to_user(decode_token(token))
        user = id_to_user(u_id)

        # user is trying to remove ownership of someone with a slackr owner/admin permission id
        if owner_user['permission_id'] > user['permission_id']:
            raise AccessError(description="User is an owner/admin of Slackr")
        # user who is trying to remove an owner when they're not an owner
        # and their permission_id is lower than the owners
        elif not user_is_owner(channel_id, owner_user['u_id']) and owner_user['permission_id'] == 3:
            raise AccessError(description="User does not have permission")
        # user is trying to remove a user who is not a owner 
        elif not user_is_owner(channel_id, u_id):
            raise ValueError(description="User is not an owner")

        channel = id_to_channel(channel_id)

        # remove the user from the owner list 
        for i in range(len(channel['owner_members'])):
            if channel['owner_members'][i]['u_id'] == u_id:
                del channel['owner_members'][i]
                break 
    
        return {}
