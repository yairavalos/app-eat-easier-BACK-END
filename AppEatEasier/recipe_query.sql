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

SELECT "App_User_Mgmt_usermenu"."id", "App_User_Mgmt_usermenu"."user_planner_id", "App_User_Mgmt_usermenu"."meal_date", 
"App_User_Mgmt_usermenu"."meal_type", "App_User_Mgmt_usermenu"."user_recipe_id", "App_User_Mgmt_usermenu"."done", 
"App_User_Mgmt_userplanner"."id", "App_User_Mgmt_userplanner"."user_profile_id", "App_User_Mgmt_userplanner"."plan_title", 
"App_User_Mgmt_userplanner"."week_num", "App_User_Mgmt_userplanner"."period", "App_User_Mgmt_userplanner"."start_date", 
"App_User_Mgmt_userplanner"."end_date", "App_User_Mgmt_userplanner"."saved", "auth_user"."id", "auth_user"."password", 
"auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", 
"auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" 
FROM "App_User_Mgmt_usermenu" 
INNER JOIN "App_User_Mgmt_userplanner" 
ON ("App_User_Mgmt_usermenu"."user_planner_id" = "App_User_Mgmt_userplanner"."id") 
INNER JOIN "auth_user" 
ON ("App_User_Mgmt_userplanner"."user_profile_id" = "auth_user"."id")
;