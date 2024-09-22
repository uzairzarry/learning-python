class UserprofileSerializer:
    def __init__(self, data):
        self.data = data

    def to_representation(self):
        return self.data

class ThoughtsSerializer:
    def __init__(self, data):
        self.data = data
        self.MyUser = UserprofileSerializer(data['MyUser'])

    def to_representation(self):
        return {
            'id': self.data['id'],
            'title': self.data['title'],
            'thought': self.data['thought'],
            'MyUser': self.MyUser.to_representation()
        }

# Create some sample data
userprofile1 = {'id': 1, 'username': 'john', 'email': 'john@example.com'}
userprofile2 = {'id': 2, 'username': 'jane', 'email': 'jane@example.com'}

thought = {
    'id': 1,
    'title': 'My Thought',
    'thought': 'This is my thought',
    'MyUser': [userprofile1, userprofile2]
}

# Create a serializer instance
serializer = ThoughtsSerializer(thought)

# Print the serialized data
print(serializer.to_representation())