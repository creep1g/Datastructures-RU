class Group:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, member):
        self.members.append(member)
    
    def get_name(self):
        return self.name

    def get_member_list(self):
        return self.members
class Person:
    def __init__(self, name):
        self.name = name
        self.group = None

class GroupedMembers:
    def __init__(self):
        self.members = dict()
        self.groups = dict()

    def add_member(self, group, name):
        if name not in self.members:
            if group not in self.groups:
                self.groups[group] = Group(group)
                self.groups[group].add_member(name)

            else:
                self.groups[group].add_member(name)

            self.members[name] = self.groups[group]

    def group_list(self, group):
        if group in self.groups:
            return self.groups[group].get_member_list()
        else:
            return []

    def member_group(self, name):
        if name in self.members:
            return self.members[name].get_name()
        else:
            return None

    def other_members_in_group(self, name):
        if name in self.members:
            member_list = self.members[name].get_member_list()
            temp = []
            for i in member_list:
                if i != name:
                    temp.append(i)

            return temp

        else:
            return []
    


#TODO: IMPLEMENT THE CLASS GroupedMembers

if __name__ == "__main__":
    gm = GroupedMembers()
    gm.add_member("G1", "maria")
    gm.add_member("G1", "lars")
    gm.add_member("G2", "celia")
    gm.add_member("G1", "dagny")
    gm.add_member("G3", "christian")
    gm.add_member("G3", "edilon")
    gm.add_member("G2", "sunna")
    gm.add_member("G4", "larus")
    gm.add_member("G4", "constantin")

    print(gm.group_list("G1"))
    print(gm.group_list("G2"))
    print(gm.group_list("G3"))
    print(gm.group_list("G4"))

    print(gm.member_group("maria"))
    print(gm.member_group("lars"))
    print(gm.member_group("celia"))
    print(gm.member_group("dagny"))
    print(gm.member_group("christian"))
    print(gm.member_group("edilon"))
    print(gm.member_group("sunna"))
    print(gm.member_group("larus"))
    print(gm.member_group("constantin"))

    print(gm.other_members_in_group("maria"))
    print(gm.other_members_in_group("lars"))
    print(gm.other_members_in_group("celia"))
    print(gm.other_members_in_group("dagny"))
    print(gm.other_members_in_group("christian"))
    print(gm.other_members_in_group("edilon"))
    print(gm.other_members_in_group("sunna"))
    print(gm.other_members_in_group("larus"))
    print(gm.other_members_in_group("constantin"))
