CLASSES
    datawiz_auth.Auth
        DW
    
    class DW(datawiz_auth.Auth)
     |  Methods defined here:
     |  
     |  get_categories_sale(self, **kwargs)
     |      Parameters:
     |      ------------
     |      categories: int,list
     |          id категорії, або список з id по яких буде робитися вибірка
     |      shops: int,list
     |          id магазину, або список з id по яких буде робитися вибірка
     |      weekday:  int {понеділок - 0, неділя - 6}
     |          день тижня по якому буде робитися вибірка
     |      date_from: datetime
     |          початкова дата вибірки
     |      date_to: datetime
     |          кінцева дата вибірки
     |          Якщо проміжок [date_from, date_to] не заданий, вибірка буде за весь час існування магазину.
     |          Якщо ж заданий тільки один з параметрів то замість іншого буде використанно перший
     |           або останій день відповідно існування магазину.
     |      interval: str,{"days","months","weeks","years", default: "days" }
     |          залежно від параметра, результат буде згруповано по днях, тижях, місяцях, або роках.
     |      by: str,
     |                  {"turnover": Оборот,
     |                  "qty": Кількість проданих товарів,
     |                  "stock_qty": Кількість товарів на залишку,
     |                  "profit": прибуток,
     |                  "stock_value": собівартість товарів на залишку,
     |                  "sold_product_value": собівартість проданих товарів,
     |          default: "turnover"}
     |          поле, по якому хочемо отримати результат вибірки.
     |      show: str,
     |                  {"name": <category_name> для назв колонок,
     |                   "id": <category_id> для назв колонок,
     |                   "both": <category_id>_<category_name> для назв колонок,
     |                   default: "name"
     |      Returns:
     |      ------------
     |          повертає об’єкт DataFrame з результатами вибірки
     |           _______________________________________
     |                   |category1|category2 |...categoryN|
     |          _______________________________________
     |           date1   |   by   |    by  |    by    |
     |           date2   |   by   |    by  |    by    |
     |           ...
     |           dateN   |   by   |    by  |    by    |
     |      
     |      Examples
     |      ------------
     |          dw = datawiz.DW()
     |          dw.get_categories_sale(categories = [50599, 50600, "sum"],by='turnover',
     |                              shops = [305, 306, 318, 321],
     |                              date_from = datetime.date(2015, 8, 9),
     |                              date_to = datetime.date(2015, 9, 9),
     |                              interval = datawiz.WEEKS)
     |                      Повернути дані обороту по категоріях з id [50599, 50600], від 9-8-2015 до 9-9-2015
     |                      по магазинах  [305, 306, 318, 321], згрупованні по тижнях
     |                      Передавши параметр "sum" останнім елементом списку, отримаємо
     |                      додаткову колонку з сумою відповідного показника
     |  
     |  get_category(self, category_id=None)
     |      Parameters:
     |      ------------
     |      category_id: int, default: None
     |      id категорії, яку вибираємо. Якщо не заданий, береться категорія найвищого рівня
     |      
     |      Returns
     |      ------------
     |      {
     |          "children": [
     |              {<child_category_id>: <child_category_name>}
     |              ...
     |              ],
     |          "category_id": <category_id>,
     |          "category_name": <category_name>,
     |          "products": [
     |              {<product_id>: <product_name>}
     |              ...
     |              ],
     |          "parent_category_id": <parent_category_id>
     |          "parent_category_name": <parent_category_name>
     |      }
     |      
     |      
     |      Examples
     |      -----------
     |      dw = datawiz.DW()
     |      dw.get_category(51171)
     |  
     |  get_client_info(self)
     |      Returns
     |      ----------
     |      Повертає інформацію про клієнта
     |      {
     |          "shops": [
     |                      {"<shop_id>": "<shop_name>"},
     |                      ...
     |                   ],
     |          "name": <client_name>,
     |          "date_from": <date_from>,
     |          "date_to": <date_to>
     |      }
     |  
     |  get_pairs(self, **kwargs)
     |      Parameters:
     |      ------------
     |      date_from: datetime
     |      Початкова дата періоду побудови пар
     |      date_to: datetime
     |      Кінцева дата періоду побудови пар
     |      shops: int, list
     |      id магазину або список магазинів
     |      hours: list [<0...23>, <0...23>, ...]
     |      Години
     |      week_day:  int<0...6>, default: "all"
     |      День тижня
     |      product_id: int
     |      id продукта
     |      category_id: int
     |      id категорії
     |      price_from: int, defaul: 0
     |      Ціна від
     |      price_to: int, default: 10000
     |      Ціна до
     |      pair_by: str, ["category", "product"], default: "category"
     |      Побудова пар для категорій чи продуктів
     |      map: int, default: 1
     |      на якому рівні рахувати супутні товари
     |      show: str, ['id', 'name', 'both'], default: 'id'
     |      Показувати id, ім’я, або обидва параметри
     |      
     |      Returns
     |      ------------
     |      Повертає об’єкт DataFrame з результатами вибірки
     |      Для параметра show = "id"
     |      
     |          ------------------------------------------
     |          0name | 1name |...| Nname | <data columns> |
     |          -------------------------------------------
     |          <id> | <id>  |...| <id>  |     <data>     |
     |      
     |          ...
     |      Для параметра show = "both"
     |      
     |          ------------------------------------------
     |          0name | 0name_name |...| Nname | Nname_name | <data_columns> |
     |          -------------------------------------------
     |          <id> |    <name>  |...| <id>  |  <name>    |   <data>       |
     |      
     |      При pair_by = "category", функція будує пари для категорій (або категорії, указаної в category_id),
     |      pair_by = "product" - для продуктів (або продукта, указаного в product_id).
     |      
     |      Examples
     |      ------------
     |      dw = datawiz.DW()
     |      dw.get_pairs(date_from = datetime.date(2015, 10, 1),
     |                  date_to = datetime.date(2015, 10, 3),
     |                  category_id = 50601,
     |                  show = 'both')
     |      Побудувати пари за період 2015, 10, 1 - 2015, 10, 3 для категорії 50601,
     |      показати id та ім’я категорій
     |  
     |  get_product(self, product_id)
     |      Parameters:
     |      ------------
     |      product_id: int
     |      
     |      Returns
     |      ------------
     |          Повертає словник в форматі json
     |      {   "category_id": <category_id>,
     |          "category_name": <category_name>,
     |          "identifier": <product_identifier>,
     |          "product_id": <product_id>,
     |          "product_name": <product_name>,
     |          "unit_id": <unit_id>,
     |          "unit_name": <unit_name>
     |      }
     |      
     |      Examples
     |      -----------
     |          dw = datawiz.DW()
     |          dw.get_product(2280001)
     |  
     |  get_products_sale(self, **kwargs)
     |      Parameters:
     |      ------------
     |      products: int,list
     |          id товару, або список з id по яких буде робитися вибірка.
     |      categories: int,list 
     |          id категорії, або список з id по яких буде робитися вибірка
     |      shops: int,list
     |          id магазину, або список з id по яких буде робитися вибірка
     |      weekday:  int {понеділок - 0, неділя - 6}
     |          день тижня по якому буде робитися вибірка
     |      date_from: datetime
     |          початкова дата вибірки
     |      date_to: datetime
     |          кінцева дата вибірки
     |          Якщо проміжок [date_from, date_to] не заданий, вибірка буде за весь час існування магазину.
     |          Якщо ж заданий тільки один з параметрів то замість іншого буде використанно перший
     |           або останій день відповідно існування магазину.
     |      interval: str,{"days","months","weeks","years", default: "days" } 
     |          залежно від параметра, результат буде згруповано по днях, тижях, місяцях, або роках.
     |      by: str,
     |                  {"turnover": Оборот,
     |                  "qty": Кількість проданих товарів,
     |                  "stock_qty": Кількість товарів на залишку,
     |                  "receipts_qty": Кількість чеків,
     |                  "profit": прибуток,
     |                  "stock_value": собівартість товарів на залишку,
     |                  "sold_product_value": собівартість проданих товарів,
     |                  "self_price_per_product": ціна за одиницю товару
     |          default: "turnover"}
     |          поле, по якому хочемо отримати результат вибірки.
     |      
     |      show: str,
     |                  {"name": <category_name> для назв колонок,
     |                   "id": <category_id> для назв колонок,
     |                   "both": <category_id>_<category_name> для назв колонок,
     |                   default: "name"
     |      
     |      Returns:
     |      ------------
     |          повертає об’єкт DataFrame з результатами вибірки
     |           _______________________________________
     |                   |product1|product2 |...productN|
     |          _______________________________________
     |           date1   |   by   |    by  |    by    |
     |           date2   |   by   |    by  |    by    |
     |           ...
     |           dateN   |   by   |    by  |    by    |
     |      
     |      Examples:
     |          dw = datawiz.DW()
     |          dw.get_products_sale(products = [2833024, 2286946, 'sum'],by='turnover',
     |                              shops = [305, 306, 318, 321], 
     |                              date_from = datetime.date(2015, 8, 9), 
     |                              date_to = datetime.date(2015, 9, 9),
     |                              interval = datawiz.WEEKS)
     |                      Повернути дані обороту по товарах з id [2833024, 2286946], від 9-8-2015 до 9-9-2015
     |                      по магазинах  [305, 306, 318, 321], згрупованні по тижнях
     |                      Передавши параметр "sum" останнім елементом списку, отримаємо
     |                      додаткову колонку з сумою відповідного показника
     |  
     |  get_receipt(self, receipt_id)
     |      Parameters:
     |      ------------
     |      receipt_id: int
     |      
     |      Returns
     |      ------------
     |          Повертає словник в форматі json
     |          {
     |              "date": <receipt_date>,
     |                  "cartitems": [{
     |                              "product_id": <product_id>,
     |                              "product_name": <product_name>,
     |                              "price": <price>,
     |                              "qty": <qty>,
     |                              "category_id": <category_id>,
     |                              "category_name": <category_name>
     |                              }],
     |              "total_price": <total_price>,
     |              "receipt_id": <receipt_id>,
     |              "loyalty_id": <loyalty_id>
     |          }
     |      
     |      Examples
     |      -----------
     |          dw = datawiz.DW()
     |          dw.get_receipt(19623631)
     |  
     |  get_receipts(self, **kwargs)
     |      Parameters:
     |      ------------
     |      products: int,list
     |          id товару, або список з id по яких буде робитися вибірка
     |      shops: int,list
     |          id магазину, або список з id по яких буде робитися вибірка
     |      weekday:  int {понеділок - 0, неділя - 6}
     |          день тижня по якому буде робитися вибірка
     |      date_from: datetime
     |          початкова дата вибірки
     |      date_to: datetime
     |          кінцева дата вибірки
     |          Якщо проміжок [date_from, date_to] не заданий, вибірка буде за весь час існування магазину.
     |          Якщо ж заданий тільки один з параметрів то замість іншого буде використанно перший
     |           або останій день відповідно існування магазину.
     |      type: str, {'full', 'short'}
     |          Тип виводу продуктів в чеку
     |          default: 'full'
     |      
     |      Returns:
     |      ------------
     |          Повертає список з чеками
     |          [
     |              {
     |               "receipt_id": <receipt_id>,
     |               "date": <receipt_datetime>,
     |               "cartitems": <cartitems>
     |               "total_price": <total_price>
     |              },
     |               ....
     |          ],
     |          де cartitems залежить від аргумента type
     |          Для type = "full" :
     |      
     |          [
     |              {
     |                  "product_id": <product_id>,
     |                  "product_name": <product_name>,
     |                  "category_id": <category_id>,
     |                  "category_name": <category_name>,
     |                  "qty": <qty>,
     |                  "price": <price>
     |              },
     |              {
     |                  "product_id": <product_id>,
     |                  "product_name": <product_name>,
     |                  "category_id": <category_id>,
     |                  "category_name": <category_name>,
     |                  "qty": <qty>,
     |                  "price": <price>
     |              }
     |              .....
     |          ]
     |      
     |          для type = "short"
     |              [<product1_id>, <product2_id>, ... , <productN_id>]
     |      
     |      
     |      Examples
     |      -------------------
     |      dw = datawiz.DW()
     |      dw.get_receipts(categories = [50599, 50600],
     |              shops = [305, 306, 318, 321],
     |              date_from = datetime.date(2015, 8, 9),
     |              date_to = datetime.date(2015, 9, 9),
     |              type = "short")
     |          Отримати всі чеки які включають продукти, що належать категоріям [50599, 50600],
     |          по магазинах [305, 306, 318, 321]
     |          за період з 2015, 8, 9  - 2015, 9, 9 в скороченому вигляді
     |  
     |  get_shops(self)
     |      Returns
     |      ----------
     |      Повертає список магазинів клієнта
     |      [ {
     |          '<shop_id>': {
     |                          "name": <shop_name>,
     |                          "area": <shop_area>,
     |                          "longitude": <shop_longitude>,
     |                          "latitude": <shop_latitude>,
     |                          "address": <shop_address>,
     |                          "open_date": <shop_open_date>
     |      
     |          }
     |          ...
     |      } ]
     |  
     |  id2name(self, id_list, typ='category')
     |      Params
     |      ------------
     |      id_list: list [<int>, <int>, <int>, ...]
     |      Список id
     |      typ: str {'category', 'products'}, default: "category"
     |      Тип id (для категорій, чи продуктів)
     |      
     |      Returns
     |      ------------
     |      Повертає словник, де ключами є id, а значеннями імена
     |      {'<category_id>': <category_name>
     |          ...
     |      }
     |      або
     |      {'<product_id>': <product_name>}
     |  
     |  name2id(self, name_list, typ='category')
     |      Params
     |      ------------
     |      name_list: list [<int>, <int>, <int>, ...]
     |      Список імен
     |      typ: str ['category', 'products'], default: "category"
     |      Тип імен (для категорій, чи продуктів)
     |      
     |      Returns
     |      ------------
     |      Повертає словник, де ключами є імена, а значеннями id
     |      {'<category_name>': <category_id>
     |          ...
     |      }
     |      або
     |      {'<product_name>': <product_id>
     |      ...
     |      }
     |  
     |  search(self, query, by='product')
     |      Parameters:
     |      ------------
     |      query: str
     |      Пошуковий запит
     |      
     |      by: str, {"category", "product",
     |                  default: "product"}
     |      Пошук по категоріям або по продуктам
     |      
     |      
     |      Returns
     |      ------------
     |      Повертає список з результатами пошуку
     |      
     |      [
     |          { <product_id>: <product_name> }
     |          { <product_id>: <product_name> }
     |          ...
     |      
     |      ]
     |      або
     |      [
     |          { <category_id>: <category_name> }
     |          { <category_id>: <category_name> }
     |          ...
     |      
     |      ]
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from datawiz_auth.Auth:
     |  
     |  __init__(self, API_KEY='test1@mail.com', API_SECRET='test2@cbe47a5c9466fe6df05f04264349f32b')

DATA
    CLIENT = 'client'
    DAYS = 'days'
    GET_CATEGORIES_SALE_URI = 'get_categories_sale'
    GET_CATEGORY = 'core-categories'
    GET_PRODUCT = 'core-products/%s'
    GET_PRODUCTS_SALE_URI = 'get_products_sale'
    GET_RECEIPT = 'core-receipts'
    INTERVALS = ['days', 'weeks', 'months', 'years']
    MODEL_FIELDS = ['turnover', 'qty', 'receipts_qty', 'stock_qty', 'profi...
    MONTHS = 'months'
    PAIRS = 'pairs'
    SEARCH = 'search'
    SHOPS = 'core-shops'
    UTILS = 'utils'
    WEEKS = 'weeks'
    YEARS = 'years'


