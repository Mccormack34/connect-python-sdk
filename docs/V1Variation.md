# V1Variation
> squareconnect.models.v1_variation

### Description

V1Variation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The item variation&#39;s unique ID. | [optional] 
**name** | **str** | The item variation&#39;s name. | [optional] 
**item_id** | **str** | The ID of the variation&#39;s associated item. | [optional] 
**ordinal** | **int** | Indicates the variation&#39;s list position when displayed in Square Register and the merchant dashboard. If more than one variation for the same item has the same ordinal value, those variations are displayed in alphabetical order | [optional] 
**pricing_type** | **str** | Indicates whether the item variation&#39;s price is fixed or determined at the time of sale. See [V1VariationPricingType](#type-v1variationpricingtype) for possible values | [optional] 
**price_money** | [**V1Money**](V1Money.md) | The item variation&#39;s price, if any. | [optional] 
**sku** | **str** | The item variation&#39;s SKU, if any. | [optional] 
**track_inventory** | **bool** | If true, inventory tracking is active for the variation. | [optional] 
**inventory_alert_type** | **str** | Indicates whether the item variation displays an alert when its inventory quantity is less than or equal to its inventory_alert_threshold. See [V1VariationInventoryAlertType](#type-v1variationinventoryalerttype) for possible values | [optional] 
**inventory_alert_threshold** | **int** | If the inventory quantity for the variation is less than or equal to this value and inventory_alert_type is LOW_QUANTITY, the variation displays an alert in the merchant dashboard. | [optional] 
**user_data** | **str** | Arbitrary metadata associated with the variation. Cannot exceed 255 characters. | [optional] 
**v2_id** | **str** | The ID of the CatalogObject in the Connect v2 API. Objects that are shared across multiple locations share the same v2 ID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


