
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi

# https://developers.facebook.com/docs/graph-api/using-graph-api/


# Token to ads_management
access_token = 'EAAF7QUK5YhoBAPGtDNYrgWa936BIouhKb5vP1ZCvY3ZAP2IHVdqlbZCQZBiZBV7s7vkHvaunOiUUite6qykubdwzDIJ1YnEtR4p6bzqZBIWZCQYsFrQuuYOiZCx6LKBAvnTs7ZCD6ZC5yyPBJ14G5gahZBMuN23OBnI5urUrddMvmfihAZDZD'
app_secret = '1378d175983f3ade228e656bb6c8f0ec'
app_id = '416995199246874'
id = '<AD_ACCOUNT_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'My campaign',
  'objective': 'LINK_CLICKS',
  'status': 'PAUSED',
}
print (AdAccount(id).create_campaign(
  fields=fields,
  params=params,
)) 

