from selenium import webdriver

# If you want to change values, you only have to change this constants, Number of Clicks is how many clicks you want
# to happen, and the upgrade is after how many clicks each time, you want to do an upgrade.
NUMBER_OF_CLICKS = 100000
UPGRADE_AFTER_CLICKS = 1000

driver = webdriver.Chrome()

driver.get('https://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element_by_id('cookie')
number_cookies = driver.find_element_by_id('money')
upgrades = ['buyTime machine', 'buyPortal', 'buyAlchemy lab', 'buyShipment', 'buyMine', 'buyFactory', 'buyGrandma',
            'buyCursor']


def buy(my_cookies):
    for item in upgrades:
        get_latest_buff = driver.find_element_by_id(item)
        item_index = 2
        if item == 'buyAlchemy lab' or item == 'buyTime machine':
            item_index = 3
        if my_cookies > int(get_latest_buff.text.split()[item_index].replace(',', '')):
            get_latest_buff.click()
            return 1


for x in range(NUMBER_OF_CLICKS):
    cookie.click()
    if (x + 1) % UPGRADE_AFTER_CLICKS == 0:
        number_converted = int(number_cookies.text.split()[0].replace(',', ''))
        buy(number_converted)
