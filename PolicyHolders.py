class PolicyHolders:
    def __init__(self, policy_id, name, email, age, phone, address, status, deleted):
        self.policy_id = policy_id
        self.name = name
        self.email = email
        self.age = age
        self.phone = phone
        self.address = address
        self.status = status #0 = deactive, 1 = active
        self.deleted = deleted #0 = active, 1 = deleted

    #source: https://pynative.com/python-class-method/
    #register
    @classmethod
    def register_policy(cls, policy_id, name, email, age, phone, address):
        # create a new policy
        # return new policy object
        return cls(policy_id, name, email, age, phone, address, 1, 0)

    #source: https://www.quora.com/How-do-you-pass-an-object-as-a-parameter-in-Python
    #deactivate/reactivate
    @classmethod
    def update_policy_status(cls, policy_data, status):
        # updates policy status
        policy_data.status = status
        # return updated policy object
        return policy_data
    
    #remove policy
    @classmethod
    def remove_policy(cls, policy_data):
        # deletes policy by setting it to 1
        policy_data.deleted = 1
        # return updated policy object
        return policy_data
