-- 코드를 입력하세요
SELECT icecream_info.flavor from icecream_info join first_half on icecream_info.flavor = first_half.flavor where first_half.total_order>=3000 and icecream_info.ingredient_type = 'fruit_based' 
# SELECT * from first_half join icecream_info on icecream_info.flavor = first_half.flavor;