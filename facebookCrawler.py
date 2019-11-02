
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi

# https://developers.facebook.com/docs/graph-api/using-graph-api/


# Token to ads_management
access_token = 'ACCESS_TOKEN>'
app_secret = 'SECRET>'
app_id = '<APP_ID>'
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

