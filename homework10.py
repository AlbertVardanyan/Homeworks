import json
# 1.
# data = {"key1" : "value1", "key2" : "value2"}

# file = json.dumps(data)
# print(file)

# # 2.
# sampleJson = """{"key1": "value1", "key2": "value2"}"""
# file = json.loads(sampleJson)
# print(file['key2'])

# 3.
# sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
# file = json.dumps(sampleJson, indent = 4, sort_keys = True)
# print(file)


# 4.
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payble":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""
# file = json.loads(sampleJson)
# print(file['company']['employee']['payble']['salary'])

# 5.

# jsonfile = """{
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payble":{ 
#             "salary":7000
#             "bonus":800
#          }
#       }
#    }
# }"""



