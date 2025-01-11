#source: https://www.geeksforgeeks.org/how-to-import-a-class-from-another-file-in-python/
#source: https://www.geeksforgeeks.org/python-call-function-from-another-file/
from PolicyHolders import PolicyHolders
from Products import Products

class Payments:
    def __init__(self, payment_id, policy_id, product_id, payment_amount, payment_date, reminder_date, reminder_sent, penalty_fee, status, deleted):
        self.payment_id = payment_id
        self.policy_id = policy_id
        self.product_id = product_id
        self.payment_amount = payment_amount
        self.payment_date = payment_date
        self.reminder_date = reminder_date
        self.reminder_sent = reminder_sent #0 = no, 1 = yes
        self.penalty_fee = penalty_fee
        self.status = status #0 = deactive, 1 = active
        self.deleted = deleted #0 = active, 1 = deleted
    
    #make payment
    @classmethod
    def make_payment(cls, payment_id, policy_id, product_id, payment_amount, payment_date, reminder_date, reminder_sent, penalty_fee):
        # create a new payment
        # return new payment object
        return cls(payment_id, policy_id, product_id, payment_amount, payment_date, reminder_date, reminder_sent, penalty_fee, 1, 0)

    #set reminder for payment
    @classmethod
    def set_payment_reminder(cls, payment_data, reminder_date):
        # updates payment status
        payment_data.reminder_date = reminder_date
        # return updated payment object
        return payment_data

    #add penalty for payment
    @classmethod
    def add_penalty_fee(cls, payment_data, penalty_fee):
        # updates payment penalty_fee
        payment_data.penalty_fee = penalty_fee
        # return updated payment object
        return payment_data
    
#Create 3 policy holders
policy_holder_1 = PolicyHolders.register_policy(1, "Musa Njie", "musa.njie@mail.com", 25, 1937278284, "Banjul")
policy_holder_2 = PolicyHolders.register_policy(2, "Mariama Janneh", "marie.janneh@mail.com", 32, 6276367834, "Bakau")
policy_holder_3 = PolicyHolders.register_policy(3, "Ousman Kassama", "ousman.kassama@mail.com", 36, 7837647647, "Brusubi")

#Create 3 products
product_1 = Products.create_product(1, "Home Insurance", "Protects your home from fire, theft, and other damages.", 1500)
product_2 = Products.create_product(2, "Car Insurance", "Provides coverage for accidents, theft, and other vehicle-related incidents.", 200)
product_3 = Products.create_product(3, "Medical Insurance", "Provides financial security for your loved ones in case of your passing.", 150)

#make payments for policy jolder 1 and 2
payment_for_policy_holder_1 = Payments.make_payment(1, policy_holder_1.policy_id, product_1.product_id, product_1.product_cost, "2024-12-10", "", 0, 0)
payment_for_policy_holder_2 = Payments.make_payment(2, policy_holder_2.policy_id, product_2.product_id, product_2.product_cost, "2024-12-10", "", 0, 0)

#source: https://favtutor.com/blogs/print-object-attributes-python
#print policy holder and payment details
policy_holder_1_details = f"Policy ID: {policy_holder_1.policy_id} \nPolicy Holder Name: {policy_holder_1.name} \nEmail: {policy_holder_1.email} \nAge: {policy_holder_1.age} \nAddress: {policy_holder_1.address} \nStatus: {policy_holder_1.status}"
policy_holder_1_payment_details = f"Payment ID: {payment_for_policy_holder_1.payment_id} \nProduct Name: {payment_for_policy_holder_1.product_id} \nAmount: {payment_for_policy_holder_1.payment_amount} \nPayment Date: {payment_for_policy_holder_1.payment_date} \nReminder Date: {payment_for_policy_holder_1.reminder_date} \nReminder Sent: {payment_for_policy_holder_1.reminder_sent} \nPenalty Fee: {payment_for_policy_holder_1.penalty_fee}"
print('----------------Policy Holder Details----------------')
print(policy_holder_1_details)
print('----------------Policy Holder Payment Details----------------')
print(policy_holder_1_payment_details)

print('\n###############################################################################################\n')

policy_holder_2_details = f"Policy ID: {policy_holder_2.policy_id} \nPolicy Holder Name: {policy_holder_2.name} \nEmail: {policy_holder_2.email} \nAge: {policy_holder_2.age} \nAddress: {policy_holder_2.address} \nStatus: {policy_holder_2.status}"
policy_holder_2_payment_details = f"Payment ID: {payment_for_policy_holder_2.payment_id} \nProduct Name: {payment_for_policy_holder_2.product_id} \nAmount: {payment_for_policy_holder_2.payment_amount} \nPayment Date: {payment_for_policy_holder_2.payment_date} \nReminder Date: {payment_for_policy_holder_2.reminder_date} \nReminder Sent: {payment_for_policy_holder_2.reminder_sent} \nPenalty Fee: {payment_for_policy_holder_2.penalty_fee}"
print('----------------Policy Holder Details----------------')
print(policy_holder_2_details)
print('----------------Policy Holder Payment Details----------------')
print(policy_holder_2_payment_details)