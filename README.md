# Salesforce API Client

## Examples

```python
from salesforce_client import SalesforceClient

sf = SalesforceClient(instance='abc.salesforce.com', session_id='')
```

```python
from salesforce_client import SalesforceClient
sf = SalesforceClient(instance_url='https://def.salesforce.com', session_id='')
```

- Authentication and authorization Examples

```python
from salesforce_client import SalesforceClient
sf = SalesforceClient(username='abc@def.com', password='password', security_token='token')
```

```python
from salesforce_client import SalesforceClient
sf = SalesforceClient(username='abc@def.com',password='password', organization_id='OrgID')
```

- For Sandbox Access

```python
from salesforce_client import SalesforceClient
sf = SalesforceClient(username='abd@c3r.com', password='adsf', security_token='token', client_id='MyAPP', domain='test')
```
