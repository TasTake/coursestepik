assert abs(-42) == -42, "Should be absolute value of a number"
assert self.is_element_present('create_class_button', timeout=30), "No create class button"
assert self.is_element_present('new_announcement_button', timeout=30), "No new announcement button on profile page"

print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))

str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

actual_result = "abrakadabra"
f"Wrong text, got {actual_result}, something wrong"

f"{2+3}"

catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
assert catalog_text == "Каталог", f"Wrong language, got {catalog_text} instead of 'Каталог'"  