from selenium import webdriver

import time

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.maximize_window()


driver.get("https://www.shufersal.co.il/online/he/A")


def Search_inputs():
#שליפת כל האינפוטים בדף ובדיקה האם מכילים את המילה חיפוש

    list_of_elements = []
    list_of_attributes = []
    list_of_elements = driver.find_elements(By.XPATH, '//input')
    flag = 0

    try:
        for element in list_of_elements:
             if flag == 0 and list_of_elements != []:
              list_of_attributes = element.get_property('attributes')
              ''' attributes = []'''
              for attribute in list_of_attributes:
                if attribute['value'].__contains__("search") or attribute['value'].__contains__("חיפוש"):
                    correct_element = element
                    flag = 1
             else:
                break
    except:
      print("no input elements! OMG!!")


    correct_element.send_keys("חלב")
    correct_element.send_keys(Keys.ENTER)


def price_search():#פונקציה המחפשת תגית כלשהי שמכילה אזכור למחיר($,מחיר,ש"ח,price)
    #אם מוצאת מחזירה את האלמנט ואם לא מחזירה 0

    print("entered price search")
    body = driver.find_elements(By.TAG_NAME, "body")
    children_of_body = body[0].find_elements(By.XPATH, ".//*")

    for element in children_of_body:
         #if element.text.__contains__("price") or element.text.__contains__("מחיר") or element.text.__contains__("$") or element.text.__contains__("₪"):
             #return element   #In case that we found an element that contains in its free text the next things:price,מחיר,$,₪
         list_of_attributes = element.get_property('attributes')
         for attribute in list_of_attributes:
             print('atribute_value'+attribute['value'])
             if attribute['value'].__contains__("price") or attribute['value'].__contains__("מחיר")or attribute['value'].__contains__("$") or attribute['value'].__contains__("₪"):
                 print('contains')
                 return element
    return 0


def search_picture1(element): #פונקציה שמקבלת אלמנט אב כלשהו של מחיר ובודקת האם מכיל אלמנט תמונה בתוכו אם מכיל יחזיר 1 ואת האלמנט של התמונה ואם לא יחזיר 0 ו0

    list_of_elements_in_the_father = element.find_elements(By.XPATH, ".//*")

    for element1 in list_of_elements_in_the_father:
        if element1.tag_name is "img" or element1.tag_name is "src" :#חיפוש האם האלמנט הוא תגית  img או src במקרה וכן יוחזר אלמנט התמונה והערך 1
            return 1,element1

    return 0, 0


# def search_picture(element): #פונקציה שמקבלת אלמנט של מחיר ובודקת האם מכיל אלמנט תמונה בתוכו בכל אלמנט תמונה שימצא יעלה את המונה ב1 בסיום הפונקציה יחזיר את המונה וכן תז של תמונה אם מצא אם לא התז יהיה 0
#
#     count1=0 #מונה
#     picture_id=0 #תז תמונה הראשונה שנמצאה
#     find_pic = 0
#
#     list_of_elements_in_the_father = element.find_elements(By.XPATH, ".//*")
#     for element1 in list_of_elements:
#         if element1.tag_name is "img" or element1.tag_name is "src" and find_pic==0:#חיפוש באלמנט אחר תגית img  או src במקרה והfind_pic  עדיין 0 סימן שזו התמונה הראשונה שנמצאה
#             count1 = count1+1
#             picture_id= element1.id
#             find_pic=1
#         else:
#             if element1.tag_name is "img" or element1.tag_name is "src":#במקרה שזו לא התמונה הראשונה שנמצאה אז רק נעלה את המונה
#                 count1 = count1 + 1
#
#     return count1, picture_id
#search_product()


def product_father(price):
    print(price)

    # flag = 0
    #
    # search_picture_results = search_picture1(can_be_the_father_element) #שליחת אובייקט האב של המחיר שנמצא לפונקציה שיחזיר 0 אם לא מצא תמונה באב ו1 אם מצא תמונה באב
    # print("can_be_the_father_element:")
    #
    # print(can_be_the_father_element)
    # while search_picture_results[0] != 1 and str(can_be_the_father_element)!="html": #ירוץ כל עוד לא נמצא באב יותר מתמונה אחת או שהאב הוא html ואנחנו כבר לא מעוניינים לעלות יותר
    #
    #     can_be_the_father_element = can_be_the_father_element #נקבל את איבר האב של האובייקט הנוכחי
    #
    #     search_picture_results = search_picture(can_be_the_father_element) # נשלח לבדיקת תמונות
    #
    # #סיבות ליציאה מהwhile :
    #
    # # -1- הגענו לתגית הhtml
    # #ז"א אין מוצרים
    # #-2- נמצאה תמונה
    #
    # if str(can_be_the_father_element) =="html":
    #     return 0 #במקרה ובחיפוש תמונה הראשוני הגענו לhtml ולא נמצאה תמונה ז"א אין מוצרים
    #
    # return  can_be_the_father_element,search_picture_results[1]
    # #במקרה ונמצאה תמונה נחזיר את האב המשותף של התמונה והמחיר וכן את אלמנט התמונה


# def find_another_pictures(element, pic_element):#פונקציה המקבלת אלמנט ואובייקט תמונה ומחפשת תמונה נוספת בתוך האלמנט שאינה התמונה שנשלחה
#
#     while str(element.tag_name) != "html":
#         list_of_elements_in_the_father = element.find_elements(By.XPATH, ".//*")
#         for element1 in list_of_elements:
#             if element1.tag_name is "img" or element1.tag_name is "src" : #בדיקה האם האלמנט הוא תמונה
#                 if element1.id != pic_element.id: # במידה והוא תמונה ואינו שווה לתמונה הראשונה שמצאנו נריץ עליו חיפוש האם הוא מכיל מחיר
#                     if check_if_the_picture_has_price(element1.parent,element)==1:
#                         return 1, element
#                     else:
#                         return 0, 0
#         element = element.parent
#
#     return 0, 0 #במקרה שמוצר יחיד


# def check_if_the_picture_has_price(element, original_element):#תחזיר 1 במידה ולתמונה יש מחיר בתוך אב שאינו האב הכולל את התמונה הראשונית ו0 במקרה שהגיעה לאב המקורי ועדיין לא מצאה מחיר ז"א שזה לא מוצר
#
#     while element.id!=original_element.id:#נרוץ כל זמן שאלמנט האב של התמונה החדשהלא שווה לאלמנט המקורי שהכיל את 2 התמונות
#         children_of_element = element.find_elements(By.XPATH, ".//*")
#         for element in children_of_element:
#          if element.text.__contains__("price") or element.text.__contains__("מחיר") or element.text.__contains__(
#                  "$") or element.text.__contains__("₪"):
#                 return 1  # In case that we found an element that contains in its free text the next things:price,מחיר,$,₪
#          list_of_attributes = element.get_property('attributes')
#          for attribute in list_of_attributes:
#             if attribute['value'].__contains__("price") or attribute['value'].__contains__(
#                     "מחיר") or element.text.__contains__("$") or element.text.__contains__("₪"):
#                 return 1
#          element=element.parent #במקרה שתגית מחיר לא נמצאה באב הספציפי נעלה אב אחד למעלה
#
#     return 0


Search_inputs()

price_element = price_search()
print(price_element.get_attribute('class'))
print(price_element)
a1 = product_father(price_element)

print("sample test case successfully completed")



