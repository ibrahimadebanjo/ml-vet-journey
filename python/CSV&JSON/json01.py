stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
# or
stringOfJsonData = '{' \
'"name": "Zophie", ' \
'"isCat": true,' \
' "miceCaught": 0,' \
' "felineIQ": null' \
'}'
import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)

# Writing JSON with the dumps() function

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 
'felineIQ': None}
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)