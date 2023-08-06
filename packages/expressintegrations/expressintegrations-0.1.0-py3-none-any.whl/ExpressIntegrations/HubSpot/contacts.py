from ..HTTP.Requests import *
from .hubspot import BASE_URL
from .hubspot import HEADERS

def create_contact(properties):
  post_url = f"{BASE_URL}contacts/v1/contact/"
  post_body = {
    'properties': format_properties(properties)
  }
  result = post(post_url, HEADERS, json.dumps(post_body))
  return result

def create_or_update_contact(email, properties):
  if not email:
    return create_contact(properties)
  post_url = f"{BASE_URL}contacts/v1/contact/createOrUpdate/email/{email}"
  post_body = {
    'properties': format_properties(properties)
  }
  result = post(post_url, HEADERS, json.dumps(post_body))
  return result

def get_all_contacts_paged(property_names, vid_offset=""):
  post_url = f"{BASE_URL}contacts/v1/lists/all/contacts/all?count=100&vidOffset={vid_offset}"
  for property_name in property_names:
    post_url = f"{post_url}&property={property_name}"
  result = get(post_url, HEADERS)
  return result

def get_all_contacts(property_names):
  contacts = []
  contact_result = get_all_contacts_paged(property_names)
  contacts_paged = contact_result['content']
  contacts += contacts_paged['contacts']
  
  while contacts_paged['has-more']:
    contact_result = get_all_contacts_paged(property_names, contacts_paged['vid-offset'])
    contacts_paged = contact_result['content']
    contacts += contacts_paged['contacts']
  
  return contacts

def get_contact_properties():
  post_url = f"{BASE_URL}properties/v1/contacts/properties"
  result = get(post_url, HEADERS)
  return result

def search_contacts_by_property_value(property_name, property_value, property_names, after=None):
  filters = [
    {
      'propertyName': property_name,
      'operator': 'EQ',
      'value': property_value
    }
  ]
  return search_contacts(property_names, filters, after)

def search_contacts_by_property_known(property_name, property_names, after=None):
  filters = [
    {
      'propertyName': property_name,
      'operator': 'HAS_PROPERTY'
    }
  ]
  return search_contacts(property_names, filters, after)

def search_contacts_by_property_less_than(property_name, property_value, property_names, after=None):
  filters = [
    {
      'propertyName': property_name,
      'operator': 'LT',
      'value': property_value
    }
  ]
  return search_contacts(property_names, filters, after)

def search_contacts_by_property_greater_than(property_name, property_value, property_names, after=None):
  filters = [
    {
      'propertyName': property_name,
      'operator': 'GT',
      'value': property_value
    }
  ]
  return search_contacts(property_names, filters, after)

def search_contacts_by_property_values(property_name, property_values, property_names, after=None):
  filters = [
    {
      'propertyName': property_name,
      'operator': 'IN',
      'values': property_values
    }
  ]
  return search_contacts(property_names, filters, after)

def search_contacts(property_names, filters, after=None):
  post_url = f"{BASE_URL}crm/v3/objects/contacts/search"
  if after:
    post_url = f"{post_url}?after={after}"
  post_body = {
    'filterGroups': [
      {
        'filters': filters
      }
    ],
    'sorts': [],
    'properties': property_names,
    'limit': 100
  }
  result = post(post_url, HEADERS, json.dumps(post_body))
  return result

def get_contact(contact_id, property_names=None, associations=None):
  post_url = f"{BASE_URL}crm/v3/objects/contacts/{contact_id}?archived=false"
  if property_names:
    post_url = f"{post_url}&properties={'%2C'.join(property_names)}"
    
  if associations:
    post_url = f"{post_url}&associations={'%2C'.join(associations)}"
  result = get(post_url, HEADERS)
  return result

def update_contact(contact_id, properties):
  post_url = f"{BASE_URL}crm/v3/objects/contacts/{contact_id}?"
  post_body = {
    'properties': properties
  }
  result = patch(post_url, HEADERS, json.dumps(post_body))
  return result