class Contact:
    """
    all_contacts： 类变量, 子类均可访问类变量。
    """
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

    def hello(self):
        print("hello, I am your daddy!")


class MailSender:
    def send_mail(self, message):
        print(f"Sending mail to {message}")


class EmailableContact(Contact, MailSender):
    pass


class Supplier(Contact):

    def order(self):
        print("this is an order")


class Friend(Contact):

    def __init__(self, name, email, phone):
        """
        name 和 email 是大家都有的属性， 可以直接调父类的初始化方法，避免重复代码
        """
        super().__init__(name, email)
        self.phone = phone
        super().hello()

    def check_contact_list(self):
        print(self.all_contacts)


if __name__ == "__main__":
    c = Contact("liang", "liang@gmail.com")

    s = Supplier("lei", "lei@gmail.com")

    f = Friend("gong", "gong@gmail.com", "11022")
    print(Contact.all_contacts)
    print(f"{f.name}:{f.email}:{f.phone}")

    f.check_contact_list()


    e = EmailableContact("ku", "ku@gmail.com")
    print(e.all_contacts)
    e.send_mail("what are you nong sha lie?")
