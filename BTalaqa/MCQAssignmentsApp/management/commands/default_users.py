from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User, Group, Permission


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        self.default_groups()
        self.default_users()

    @staticmethod
    def default_groups():
        """
        adds two default groups:

         - Teachers
         - Students

        :return:
        """
        st_group = Group.objects.create(name='Students')
        for codename in ('read_test', 'read_question', 'read_answer'):
            permission = Permission.objects.get(
                codename=codename,
            )
            st_group.permissions.add(permission)

        th_group = Group.objects.create(name='Teachers')
        for codename in ('edit_test', 'edit_question', 'edit_answer'):
            permission = Permission.objects.get(
                codename=codename,
            )
            th_group.permissions.add(permission)

    @staticmethod
    def default_users():
        user = User.objects.create_user(username='user',
                                        email='user@email.com',
                                        password='user')
        user.save()
        group = Group.objects.get(name='Students')
        group.user_set.add(user)

        auser = User.objects.create_user(username='admin',
                                         email='admin@email.com',
                                         is_staff=True,
                                         password='admin')
        auser.save()
        group = Group.objects.get(name='Teachers')
        group.user_set.add(auser)

        suser = User.objects.create_user(username='superadmin',
                                         email='admin@email.com',
                                         is_staff=True,
                                         is_superuser=True,
                                         password='superadmin')
        suser.save()
