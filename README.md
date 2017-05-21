# Tech2Grow
Tech 2 Grow Hackathon code

![alt text](http://res.cloudinary.com/ideation/image/upload/w_128,h_128/msw8en1atvrz1ytwrrrd.png)


## Project Name: ShoppiLens 
## Team : Dream way
## Members : Aymen.Z & Nidhal.S & Anis.H


## Description:



## Features

- Indoor navigation through products departments

![alt text](http://www.hostingpics.net/viewer.php?id=338596UntitledDiagram1.png)

	We will use the below Products/Categories location data to build an indoor navigation system. The person initial position will be detected through wifi connection. Then, according to the list of items he dictated to ShoppiLens, the system calculates the shortest path throughout the store to pick up the products he wants.
	This path will be detailed to the user incrimentely as he wlaks in throurgh store's department voccaly.
	The user position wil be indentified based on Wifi postioning (triangulation) system.

- Code Organization

|   FILE   | Description |
|:--------:|-------------|
| main     |  module for data reading, naviguation graph building and processing|
| notebook |  data exploration and script testing|

![alt text](http://oi68.tinypic.com/2rrnpg6.jpg)

	Whe have modilized the store department as a graph.
	Nodes represent Products's Categories.
	Every node (category) is an inner Graph of products 




- Speech 2 text
	Using Google speech API, we send and detect the user vocal request.
	The voice will be analysed and converted to a list of items or categories to purchase.


- Text 2 speech
	To connect with the user, our system use the voice instructions to guide the user through his way and descibe detected products.



## Used data:

The data : 


│   │   ├── PRODUCT_CLASSIFICATION.txt
                Header : HYP_GRP_CLASS_KEY|HYP_GRP_CLASS_DESC|HYP_CLASS_KEY|HYP_CLASS_DESC|HYP_SUB_CLASS_KEY|HYP_SUB_CLASS_DESC|HYP_CLUST_CLASS_DESC
		
				HYP_SUB_CLASS_KEY           HyperMarket unique identifier of a product sub-class (Sub-Family)
                HYP_SUB_CLASS_DESC          HyperMarket product sub-class (Sub-Family) description
                HYP_CLASS_KEY               HyperMarket unique ID for Class (Product Family)
                HYP_CLASS_DESC              HyperMarket class (Product Family) description
                HYP_GRP_CLASS_KEY           HyperMarket unique ID for Group Class (Product Group Family)
                HYP_GRP_CLASS_DESC          HyperMarket group Class (Product Group Family) description
                HYP_CLUST_CLASS_DESC        Cluster of several group Classes consistent (Product Group Family) description


│   │   ├── STORE_CATEGORY_LOCALIZATION.txt
                Header : STORE_KEY|HYP_GRP_CLASS_KEY|HYP_GRP_CLASS_DESC|ABSCISSA|ORDINATE|HEIGHT

                STORE_KEY             	    Store Thales Code
				HYP_GRP_CLASS_KEY	    	HyperMarket unique ID for Group Class (Product Group Family)
				HYP_GRP_CLASS_DESC	    	HyperMarket group Class (Product Group Family) description
				ABSCISSA					Location of a given product in the store defined by a number between 0 and 1000, corresponding to the minimum and maximum of a store picture 
				ORDINATE					Location of a given product in the store defined by a number between 0 and 1000, corresponding to the minimum and maximum of a store picture 
				HEIGHT						Height of a given product in the store defined by a number. The value is always 0


│   │   ├── STORE_PERMANENT_PRODUCT_LOCALIZATION.txt
                Header : ITEM_KEY|ITEM_DESC|HYP_DEPARTMENT_KEY|PRD_CAPA_TYPE||SELL_PRICE|PROMO_FLAG|UNIT_SELL_PRICE|ABSCISSA|ORDINATE|HEIGHT

				ITEM_KEY		    		Barcode of the product, Global Trade Item Number (GTIN)
				ITEM_DESC		    		Description of the product
				HYP_DEPARTMENT_KEY	    	HyperMarket unique identifier of a product sub-class (Sub-Family)
				PRD_CAPA_TYPE
				SELL_PRICE		    		Current sales price for a given product, in euro cents
				PROMO_FLAG		    		If product is in promotion period for the day, then 1, otherwise 0
				UNIT_SELL_PRICE		   	 	Current sales price for a given product, in euro cents divided by the capacity
				ABSCISSA		    		Location of a given product in the store defined by a number between 0 and 1000, corresponding to the minimum and maximum of a store picture 
				ORDINATE		    		Location of a given product in the store defined by a number between 0 and 1000, corresponding to the minimum and maximum of a store picture 
				HEIGHT			    		Height of a given product in the store defined by a number. The value is always 0


│   │   ├── STORE_PROMOTION_PRODUCT_LOCALIZATION.txt
                Header : STORE_KEY|ITEM_KEY|ITEM_DESC|BRAND_DESC|ABSCISSA|ORDINATE|HEIGHT

				STORE_KEY             	    Store Thales Code
				ITEM_KEY		    		Barcode of the product, Global Trade Item Number (GTIN)
				ITEM_DESC		    		Description of the product
				BRAND_DESC		    		HyperMarket unique identifier of a product sub-class (Sub-Family)
				ABSCISSA		    		Location of a given product in the store defined by a number between 0 and 1000, corresponding to the minimum and maximum of a store picture 
				ORDINATE		    		Location of a given product in the store defined by a number between 0 and 1000, corresponding to the minimum and maximum of a store picture 
				HEIGHT			    		Height of a given product in the store defined by a number. The value is always 0

		
│   │   └── FRA118_MAP.png
