-- SQLite
SELECT App_Recipe_Mgmt_catalogrecipe.id, App_Recipe_Mgmt_catalogrecipe.title, App_Recipe_Mgmt_catalogrecipe.meal_type,
App_Recipe_Mgmt_recipeingredient.id, App_Recipe_Mgmt_recipeingredient.cat_ingredient_id,
App_SprMkt_Mgmt_catalogingredient.id, App_SprMkt_Mgmt_catalogingredient.ingredient_cat, App_SprMkt_Mgmt_catalogingredient.ingredient_name
FROM App_Recipe_Mgmt_catalogrecipe
INNER JOIN App_Recipe_Mgmt_recipeingredient
ON App_Recipe_Mgmt_recipeingredient.cat_recipe_id = App_Recipe_Mgmt_catalogrecipe.id
INNER JOIN App_SprMkt_Mgmt_catalogingredient
ON App_SprMkt_Mgmt_catalogingredient.id = App_Recipe_Mgmt_recipeingredient.cat_ingredient_id
;

SELECT App_Recipe_Mgmt_catalogrecipe.id, App_Recipe_Mgmt_catalogrecipe.title, App_Recipe_Mgmt_catalogrecipe.meal_type,
App_Recipe_Mgmt_recipeingredient.id, 
App_Recipe_Mgmt_recipeingredient.ingredient_qty, App_SprMkt_Mgmt_unitsconvertion.equivalency,
App_SprMkt_Mgmt_catalogingredient.id, App_SprMkt_Mgmt_catalogingredient.ingredient_cat, 
App_SprMkt_Mgmt_catalogingredient.ingredient_name, App_SprMkt_Mgmt_sprmktpackaging.spq_value, 
App_SprMkt_Mgmt_sprmktpackaging.unit_type_id, App_SprMkt_Mgmt_sprmktpackaging.package_type_id
FROM App_Recipe_Mgmt_catalogrecipe
INNER JOIN App_Recipe_Mgmt_recipeingredient
ON App_Recipe_Mgmt_recipeingredient.cat_recipe_id = App_Recipe_Mgmt_catalogrecipe.id
INNER JOIN App_SprMkt_Mgmt_catalogingredient
ON App_SprMkt_Mgmt_catalogingredient.id = App_Recipe_Mgmt_recipeingredient.cat_ingredient_id
INNER JOIN App_SprMkt_Mgmt_unitsconvertion
ON App_SprMkt_Mgmt_unitsconvertion.id = App_Recipe_Mgmt_recipeingredient.unit_type_id
INNER JOIN App_SprMkt_Mgmt_sprmktpackaging
ON App_SprMkt_Mgmt_sprmktpackaging.ingredient_id = App_Recipe_Mgmt_recipeingredient.cat_ingredient_id
;