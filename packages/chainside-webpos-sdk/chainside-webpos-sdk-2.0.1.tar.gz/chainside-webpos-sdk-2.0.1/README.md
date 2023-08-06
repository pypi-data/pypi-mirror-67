<!--
Nigiri auto-generated file
-->
<p>
<img src="https://www.chainside.net/wp-content/themes/chainside2018/assets/favicon//favicon-192.png" alt="chainside" width="80">
<br \><br \>
developed with :heart: by <a href="https://www.chainside.net">chainside</a>
</p>


<!-- START doctoc -->
<!-- END doctoc  -->

# Introduction

This project is the **official** SDK library for the integration with the [Chainside Pay]() Platform.
It is an extension of the [Sdk-boilerplate]() library.
 
# Installation

Follow these steps to install the SDK library into your system:

```bash
pip install chainside-webpos-sdk 
```

In order to configure the redis cache backend, you must install the redis server and the python
client. (For further information, check the https://redis.io/ documentation)

Installing redis server:

Apt:

```bash
apt install redis-server
```
Brew:

```bash
brew install redis
```

Then, to install the python client
```bash
pip install redis
```

# Structure

The following sections will describe the high level structure of the
SDK library.

## Configuration

In order to be able to configure your SDK client you have to set some
configuration parameters. Here is the list of the configuration parameters
used by the library:

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| **mode** | _string_ | Yes | `live` | The SDK mode, can be `sandbox` or `live` |
| **client_id** | _string_ | Yes | `null` | Your WebPos client id |
| **secret** | _string_ | Yes | `null` | Your WebPos secret |
| **http** |  |  | Http further configuration |
 
_http_ is a further configuration for the actual sending of requests. It can be configured
 by specifying the following parameters (if not specified, a default is provided)
 
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| **verify_ssl** | _string_ | No | true | Wheter to perform ssl verification  |
| **timeout** | _integer_ | No | 10 | Timeout on sent requests (seconds) |

A cache adapter can be configured aswell (if not, a default cache adapter is provided from the sdk).
The configuration must define the following parameters:

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| **driver** | _string_ | No | `dict` | The cache driver to be used |
| **options** | _dict_ | No | `null` | Cache driver further configuration |

Driver can be either 'redis', 'django' or the default 'dict'.
If redis is configured as a driver, the options configuration parameters are the following:

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| **hostname** | _string_ | No | localhost | Hostname of the redis server |
| **port** | _integer_ | No | 6379 | Port of the redis server |
| **password** | _string_ | No | `null` | Password to connect to the redis server |
| **decode_responses** | _boolean_ | No | True | Wheter to return byte or decoded responses |

For django or dict cache adapters, no further configuration is needed.
If django is selected, the adapter wraps the django.core.cache cache singleton
If dict is selected, (or the cache driver is not specified ), the sdk instantiates a DictCacheAdapter
object which is a singleton in the application and uses a dictionary to store values.


## Client

The Library exposes a _client_ object which is instantiated with the system configuration and
provides an high-level interface to send requests. Client's instances take care of compiling and
sending http request and parse responses into [SdkObject](#Objects) instances. 

## Objects

The library defines an SdkObject class which is extended by actual objects which represent Chainside-Pay
API requests and response bodies. Every json object defined in the API has a corresponding SdkObject
class which is either the input of a _client_ instance method (for creation) or returned (for reading)

## Callbacks

Callbacks are requests sent by the server to your application in order to notify about some events. 
Every callback is sent **only to HTTPS** webhooks and will be securely signed by the server in order to be verified.

# Usage

The following sections will describe how to use the SDK library and
all the detail needed to integrate your business with Chainside Pay.

## Instantiate and use the client

In order to communicate with our backend first you need to instantiate
the client:

```python
from webpos_sdk.client import Client
from webpos_sdk.objects import PaymentOrder
conf = {
        'mode' : 'live',
        'client_id' : '${webpos_client_id}',
        'secret' : '${webpos_secret}',
        ...
        }
client = Client(conf)
payment_order = PaymentOrder(
                                amount='10.00',
                                continue_url='https://continue.com',
                                ...
                            )
response = client.create_payment_order(payment_order)                            
```


Once the client is instantiated and configured, you can use the following
methods to send requests:


| Method |
|--------|
| `delete_payment_order`(payment_order_uuid:uuid) : [PaymentOrderResponse](#PaymentOrderResponse)| 
| `get_payment_order`(payment_order_uuid:uuid) : [PaymentOrderRetrieval](#PaymentOrderRetrieval)| 
| `get_payment_orders`(page:integer=None,sort_order:string=None,sort_by:string=None,status:string=None,page_size:integer=None) : [PaymentOrderList](#PaymentOrderList)| 
| `create_payment_order`(payment_order:PaymentOrder) : [PaymentOrderResponse](#PaymentOrderResponse)| 
| `get_callbacks`(payment_order_uuid:uuid) : [CallbackList](#CallbackList)| 
| `payment_reset`(payment_order_uuid:uuid) : [PaymentOrderRetrieval](#PaymentOrderRetrieval)| 
| `payment_update`(payment_order_uuid:uuid,payment_update_object:PaymentUpdateObject) : [None](#None)| 
| `client_credentials_login`(client_credentials:ClientCredentials) : [ClientCredentialsLoginResponse](#ClientCredentialsLoginResponse)| 



## Objects

### PaymentOrderDeletionResponse

Payment order deletion response

#### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| cancel_url | _string_ | Yes | The URL where the user is redirected upon payment order expiration/cancellation |


### PaymentOrderRetrieval

Payment order retrieval data

#### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| redirect_url | _string_ | No | URL where to redirect the user to perform the payment |
| resolved_at | _string_ | Yes | Time at which either the payment order has been fully paid or is expired |
| created_at | _string_ | Yes | Creation date of the payment order |
| btc_amount | _integer_ | Yes |  Bitcoin amount of the payment order |
| details | _string_ | No | Payment order's details |
| uri | _string_ | Yes | Bitcoin uri |
| state | _[PaymentOrderState](#paymentorderstate)_ | Yes | Current payment state of the payment order |
| created_by | _[PaymentOrderCreator](#paymentordercreator)_ | Yes | Data of the pos which created the payment order |
| amount | _string_ | Yes | Fiat's amount of the payment order |
| dispute_start_date | _string_ | Yes | Time at which either the payment order has been fully paid or is expired |
| address | _string_ | Yes | Bitcoin address of the payment order |
| chargeback_date | _string_ | Yes | Time at which either the payment order has been fully paid or is expired |
| rate | _[RateRetrieval](#rateretrieval)_ | Yes | Crypto/Fiat rate of the payment order |
| required_confirmations | _integer_ | Yes | Required confirmations for transactions paying the payment order |
| transactions | _[[Transaction](#Transaction)]_ | Yes | Transactions paying the payment order |
| uuid | _string_ | Yes | UUID of the payment order |
| reference | _string_ | Yes | Business' reference for the payment order |
| expires_in | _integer_ | Yes |  Expiration time of the payment order |
| callback_url | _string_ | No | The URL contacted to send callbacks related to payment status changes |
| currency | _[CurrencyRetrieval](#currencyretrieval)_ | Yes | Fiat currency of the payment order |
| expiration_time | _string_ | Yes | Expiration date of the payment order |


### PaymentOrderState

Data describing the current state of a payment order

#### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| unpaid | _[PaidStatus](#paidstatus)_ | Yes | Payment order's unpaid amount |
| paid | _[PaidStatus](#paidstatus)_ | Yes | Payment order's paid amount |
| blockchain_status | _string_ | Yes | Payment order's internal status |
| status | _string_ | Yes | Payment order's status |
| in_confirmation | _[PaidStatus](#paidstatus)_ | Yes | Payment order's paid but unconfirmed amount |


### PaidStatus

Cryto and fiat paid amounts

#### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| fiat | _string_ | Yes | Fiat Amount |
| crypto | _integer_ | Yes | Cryto Amount |


### PaymentOrderCreator

Data of payment order's creator

#### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| active | _bool_ | No | Wheter the creator active |
| type | _string_ | Yes | Payment order creator's type |
| deposit_account | _[DepositAccountLite](#depositaccountlite)_ | Yes | Deposit account associated to the payment order's creator |
| name | _string_ | Yes | Payment order creator's name |
| uuid | _string_ | Yes | Payment order creator's uuid |


### DepositAccountLite

Deposit account lite object when sent nested in other api objects

#### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| type | _string_ | Yes | Deposit account's type |
| name | _string_ | Yes | Deposit account's name |
| uuid | _string_ | Yes | Deposit account's uuid |


### RateRetrieval

Rate Data

#### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| from | _string_ | No | Starting currency for rate calculation |
| created_at | _string_ | Yes | Creation's date of the rate |
| value | _string_ | Yes | Value of the rate |
| to | _string_ | No | Target currency for rate calculation |
| source | _string_ | Yes | Exchange providing the rate |


### Transaction

Bitcoin transaction paying a payment order

#### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| outs_sum | _integer_ | Yes | Paying amount of the transaction |
| status | _string_ | Yes | Transaction's status |
| created_at | _string_ | Yes |  |
| txid | _string_ | Yes | Transaction's id |
| outs | _[[Out](#Out)]_ | Yes | Transaction's outputs |
| normalized_txid | _string_ | Yes | Transaction's normalized id |
| blockchain_status | _string_ | Yes | Transaction's internal status |


### Out

Transaction's output

#### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| n | _integer_ | Yes | Transaction output's index |
| amount | _integer_ | Yes | Output's amount |


### CurrencyRetrieval

Currency Data

#### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| type | _string_ | Yes | Currency's type (fiat/crypto) |
| name | _string_ | Yes | Name of the currency |
| uuid | _string_ | Yes | UUID of the currency |


### PaymentOrderList

List of Business' payment orders

#### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| paymentorders | _[[PaymentOrderRetrieval](#PaymentOrderRetrieval)]_ | Yes | Business' payment orders |
| total_pages | _integer_ | Yes | Total number of pages given the requested page size |
| total_items | _integer_ | Yes | Total number of items |


### PaymentOrderCreation

Data required to create a new payment order

#### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| reference | _string_ | No | Business' reference of the payment order |
| cancel_url | _string_ | No | The URL where the user is redirected upon successful payment order expiration/cancellation |
| callback_url | _string_ | No | The URL contacted to send callbacks related to payment status changes |
| required_confirmations | _integer_ | No | Required confirmations for transactions paying the payment order |
| continue_url | _string_ | No | The URL where the user is redirected upon successful payment |
| amount | _string_ | Yes | Payment order's fiat amount |
| details | _string_ | No | Payment order's details |


### PaymentOrderCreationResponse

Response data for a payment order creation request

#### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| address | _string_ | Yes | Bitcoin address of the payment order |
| redirect_url | _string_ | Yes | URL where to redirect the user to perform the payment |
| rate | _[RateRetrieval](#rateretrieval)_ | Yes | Crypto/Fiat rate of the payment order |
| created_at | _string_ | No | Creation date of the payment order |
| uuid | _string_ | Yes | UUID of the payment order |
| reference | _string_ | No | Payment Order reference |
| expires_in | _integer_ | Yes | Expiration's time of the payment order |
| uri | _string_ | Yes | Bitcoin uri according to BIP 21 (https://github.com/bitcoin/bips/blob/master/bip-0021.mediawiki) |
| amount | _integer_ | Yes | Crypto amount of the payment order |
| expiration_time | _string_ | Yes | Expiration's date of the payment order |


### CallbackList

Callback list object

#### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| callbacks | _[[Callback](#Callback)]_ | Yes | Valid payment transitions callbacks |


### Callback

Callback Retrieval object

#### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| name | _string_ | Yes | Namespace of a callback sent after the related payment status' transition |


### PaymentUpdateObject

Callback's trigger request body

#### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| callback | _string_ | Yes | Name of the callback to be sent |


### ClientCredentials

Data required to perform a confidential client login

#### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| scope | _string_ | Yes | Oauth2 scope of the client's authorization |
| grant_type | _string_ | Yes | Oauth2 Authorization's grant type |


### ClientCredentialsLoginResponse

Response data for a login performed by a confidential client.

#### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| id_token | _string_ | Yes | Jwt Token containing identity's informations |
| expires_in | _integer_ | Yes | Token's expiration time |
| access_token | _string_ | Yes | User's access token |
| token_type | _string_ | Yes | Token's type |
| scope | _string_ | No | Authorization's scope |


### CallbackPaymentOrder

Payment order retrieval data

#### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| redirect_url | _string_ | Yes | URL where to redirect the user to perform the payment |
| resolved_at | _string_ | Yes | Time at which either the payment order has been fully paid or is expired |
| created_at | _string_ | Yes | Creation date of the payment order |
| btc_amount | _integer_ | Yes |  Bitcoin amount of the payment order |
| details | _string_ | Yes | Payment order's details |
| uri | _string_ | Yes | Bitcoin uri |
| state | _[PaymentOrderState](#paymentorderstate)_ | Yes | Current payment state of the payment order |
| created_by | _[PaymentOrderCreator](#paymentordercreator)_ | Yes | Data of the pos which created the payment order |
| amount | _string_ | Yes | Fiat's amount of the payment order |
| dispute_start_date | _string_ | Yes | Time at which either the payment order has been fully paid or is expired |
| address | _string_ | Yes | Bitcoin address of the payment order |
| chargeback_date | _string_ | Yes | Time at which either the payment order has been fully paid or is expired |
| rate | _[RateRetrieval](#rateretrieval)_ | Yes | Crypto/Fiat rate of the payment order |
| cancel_url | _string_ | Yes | The URL where the user is redirected upon payment order expiration/cancellation |
| required_confirmations | _integer_ | Yes | Required confirmations for transactions paying the payment order |
| transactions | _[[Transaction](#Transaction)]_ | Yes | Transactions paying the payment order |
| uuid | _string_ | Yes | UUID of the payment order |
| reference | _string_ | Yes | Business' reference for the payment order |
| expires_in | _integer_ | Yes |  Expiration time of the payment order |
| callback_url | _string_ | Yes | The URL contacted to send callbacks related to payment status changes |
| currency | _[CurrencyRetrieval](#currencyretrieval)_ | Yes | Fiat currency of the payment order |
| expiration_time | _string_ | Yes | Expiration date of the payment order |
| continue_url | _string_ | Yes | The URL where the user is redirected upon successful payment |


## Exceptions

Every exception raised due to an error response contains debug informations.

```python
from webpos_sdk.exceptions import SdkHttpException

try:
    client.create_payment_order(payment)
except SdkHttpException as e:
    print(e.debug_info)
    print(e.request_id)

```

Debug Info contains general information about request and response headers, body and status code. 
Request Id is an internal id which can be communicated to chainside in order to help debugging the problem in case this cannot be identified.



## Callbacks

Chainside will send callbacks if some event is triggered regarding one of your assets registered on the Business Panel.
Our server will send a request to your webhooks that you need to parse and verify. You can do this using this SDK library
in the following way:

```python
from webpos_sdk.callbacks.handler import ChainsideCallbacksHandler
from webpos_sdk.api_context import ChainsideApiContext

conf = {
        'mode' : 'live',
        'client_id' : '${webpos_client_id}',
        'secret' : '${webpos_secret}',
        ...
        }
context = ChainsideApiContext(conf)
handler = ChainsideCallbacksHandler(context)
callback_sdk_object = handler.parse(request.headers, request.body) 
# The request body should be the raw body ( in bytes ) of the request since it's used to compute the signature
```

### Callback structure

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| created_at | _string_ | Yes | Date in which the callback was sent |
| event | _string_ | Yes | Event which triggered the callback |
| object_type | _string_ | Yes | Type of the object sent in the callback |
| object | [CallbackPaymentOrder](#callbackpaymentorder) | Yes |  |


### Triggered events

| Event | Object Class |
|------------|--------------|
| `payment.completed` | [CallbackPaymentOrder](#callbackpaymentorder) |
| `payment.dispute.start` | [CallbackPaymentOrder](#callbackpaymentorder) |
| `payment.overpaid` | [CallbackPaymentOrder](#callbackpaymentorder) |
| `payment.cancelled` | [CallbackPaymentOrder](#callbackpaymentorder) |
| `payment.dispute.end` | [CallbackPaymentOrder](#callbackpaymentorder) |
| `payment.expired` | [CallbackPaymentOrder](#callbackpaymentorder) |
| `payment.chargeback` | [CallbackPaymentOrder](#callbackpaymentorder) |


# Changelog
    2.0.0 : 
        - Add request_id and debug_info to raised exceptions
        - Add pagination to payment order retrieval method
        - Replace the payment orders retrieval endpoint 
                
# Contributing

In order to maintain consistency between our backend and our SDKs, contributing through pull requests is highly
discouraged. Consider posting an issue if you need to signal any problem with this library.

# Security Issues

In case of a discovery of an actual or potential security issue please contact us at [info@chainside.net](mailto:info@chaniside.net)

