contact_book={
    "Alice":{
        "Phone Number": 2345678,
        "Email": "alice@gmail.com",
        "Tags": ["work", "friend"]
    },
    "Bob":{
        "Phone Number": 2345678,
        "Email": "alice@gmail.com",
        "Tags": ["work"]
    },
    "noor":{
        "Phone Number": 2345678,
        "Email": "alice@gmail.com",
        "Tags": ["work", "family"]
    }
}
for key, value in contact_book.items():
    print(f"Contact: {key} | {value}")

user_name= input("Enter Name: ")
user_number= input("Enter Phone Number: ")
user_email= input("Enter user's email: ")
user_tags = input("Enter tags separated by commas: ")

contact_book[user_name]={
    "Phone number": user_number,
    "Email": user_email,
    "Tags": user_tags.split(',')
}
print(f"Name: {user_name} with Phone number: {user_number} and email: {user_email} and tags: {user_tags} has been added to your contact list.")
# print(f"Updated list is: {contact_book}")

search_name=input("Enter the Contact name you want to search: ")
result=contact_book.get(search_name)
if result:
    print(f"{search_name} | {result}")
else:
    print(f"Sorry {search_name} was not found in your contacts")

delete_contact= input("Enter the name you want to delete: ")

if delete_contact in contact_book:
    deleted=contact_book.pop(delete_contact)
    print(f"{delete_contact}  has been deleted from contact")
    # print(f"Updated list is: {contact_book}")
else:
    print(f"'{delete_contact}' not found in your contact")



def get_unique_tags(contact_book):
    unique_tags = set()
    for info in contact_book.values():
        unique_tags.update(info["Tags"]) 
    return unique_tags


print("Unique tags across all contacts:", get_unique_tags(contact_book))
