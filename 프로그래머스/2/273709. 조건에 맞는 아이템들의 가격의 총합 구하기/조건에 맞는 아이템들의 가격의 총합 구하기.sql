-- 코드를 작성해주세요
select sum(PRICE) as TOTAL_PRICE
from item_info
WHERE RARITY = 'LEGEND'