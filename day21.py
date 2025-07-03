# # # Access modifier
# # # protected access modifier
# # class A():
# #     _test="hello"

# # class B(A):
# #     def test(self):
# #         return self._test


# # obj = B()
# # print(obj.test())



# # Access modifier
# # private access modifier
# class A():
#     __test="hello"
#     test1 = __test

#     def __hello(self):
#         print(self.__test)
#         print("hello")

#     def test2(self):
#         self.__hello()





# obj = A()
# print(obj.test1)

# # class B(A):
# #     def test(self):
# #         return self.test2()

# #     # def console(self):
# #     #     print(self.__hello())


# # obj = B()
# # print(obj.test())
# # # print(obj.console())



a = "name"
# b = "hel÷lo"
# try and except


try:
    print(1/y)
except NameError as e:
    print(e)
except ValueError as e:
    print(e)
except:
    print("something went wrong")