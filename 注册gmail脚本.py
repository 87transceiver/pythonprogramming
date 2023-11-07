from selenium import webdriver
import time

def register_gmail(email, password):
    # 设置Chrome浏览器驱动路径
    driver_path = 'path_to_your_chrome_driver'  # 请将路径替换为您本地Chrome驱动的实际路径
    driver = webdriver.Chrome(executable_path=driver_path)

    # 打开Gmail注册页面
    driver.get('https://accounts.google.com/signup')

    # 输入邮箱地址和密码
    email_input = driver.find_element_by_xpath('//*[@id="username"]')
    email_input.send_keys(email)

    password_input = driver.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input')
    password_input.send_keys(password)

    confirm_password_input = driver.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
    confirm_password_input.send_keys(password)

    # 点击“下一步”按钮
    next_button = driver.find_element_by_xpath('//*[@id="accountDetailsNext"]')
    next_button.click()

    # 等待一段时间，确保页面加载完成
    time.sleep(5)

    # 输入用户信息（这一步因国家和地区不同，可能会有额外的信息填写）
    first_name_input = driver.find_element_by_xpath('//*[@id="firstName"]')
    first_name_input.send_keys('Your First Name')

    last_name_input = driver.find_element_by_xpath('//*[@id="lastName"]')
    last_name_input.send_keys('Your Last Name')

    # 点击“下一步”按钮
    next_button = driver.find_element_by_xpath('//*[@id="accountDetailsNext"]')
    next_button.click()

    # 等待一段时间，确保页面加载完成
    time.sleep(5)

    # 输入手机号码（这一步因国家和地区不同，可能会有额外的信息填写）
    phone_input = driver.find_element_by_xpath('//*[@id="phoneNumberId"]')
    phone_input.send_keys('Your Phone Number')

    # 点击“下一步”按钮
    next_button = driver.find_element_by_xpath('//*[@id="gradsIdvPhoneNext"]')
    next_button.click()

    # 等待一段时间，确保页面加载完成
    time.sleep(5)

    # 输入验证码（这一步因国家和地区不同，可能会有额外的信息填写）
    # 这里需要手动输入验证码，所以在自动化脚本中无法完成该步骤

    # 点击“下一步”按钮
    next_button = driver.find_element_by_xpath('//*[@id="gradsIdvVerifyNext"]')
    next_button.click()

    # 等待一段时间，确保页面加载完成
    time.sleep(5)

    # 完成注册（点击“我同意”按钮）
    agree_button = driver.find_element_by_xpath('//*[@id="termsofserviceNext"]')
    agree_button.click()

    # 等待一段时间，确保页面加载完成
    time.sleep(5)

    # 关闭浏览器
    driver.quit()

if __name__ == "__main__":
    # 填写您要注册的邮箱地址和密码
    email_address = 'your_email_address@gmail.com'
    password = 'your_password'
    register_gmail(email_address, password)
