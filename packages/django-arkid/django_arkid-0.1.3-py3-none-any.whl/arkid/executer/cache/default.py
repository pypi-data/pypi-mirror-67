'''
操作对默认缓存的影响
'''

from django.core.cache import cache
from django_redis import get_redis_connection

from ...executer.core import Executer
from ...tasksapp.tasks import (
    update_users_cache,
    update_nodes_cache,
)


class CacheExecuter(Executer):
    '''
    更新缓存
    '''
    def create_user(self, user_info):
        '''
        目前不影响缓存
        '''

    def update_user(self, user, user_info):
        '''
        目前不影响缓存
        '''

    def set_user_password(self, user, plaintext):
        '''
        目前不影响缓存
        '''

    def delete_users(self, users):
        '''
        批量删除用户
        删除缓存
        '''
        redis_conn = get_redis_connection('default')
        pipe = redis_conn.pipeline()
        for user in users:
            key = cache.client.make_key(f'oneid:user:{user.username}:parent_node')
            pipe.delete(key)
            key = cache.client.make_key(f'oneid:user:{user.username}:upstream_node')
            pipe.delete(key)
        pipe.execute()

    def create_dept(self, dept_info):
        '''
        目前不影响缓存
        '''

    def update_dept(self, dept, dept_info):
        '''
        目前不影响缓存
        '''

    def delete_dept(self, dept):
        '''
        删除部门
        删除缓存
        '''
        key = f'oneid:node:{dept.node_uid}:upstream'
        cache.delete(key)

    def create_group(self, group_info):
        '''
        目前不影响缓存
        '''

    def update_group(self, group, group_info):
        '''
        目前不影响缓存
        '''

    def delete_group(self, group):
        '''
        删除组
        删除缓存
        '''
        key = f'oneid:node:{group.node_uid}:upstream'
        cache.delete(key)

    def add_users_to_dept(self, users, dept):
        '''
        更新用户缓存
        '''
        update_users_cache.delay([user.username for user in users])

    def sort_users_in_dept(self, users, dept):
        '''
        目前不影响缓存
        '''

    def add_user_to_depts(self, user, depts):
        '''
        更新用户缓存
        '''
        update_users_cache.delay([user.username])

    def delete_users_from_dept(self, users, dept):
        '''
        更新用户缓存
        '''
        update_users_cache.delay([user.username for user in users])

    def delete_user_from_depts(self, user, depts):
        '''
        更新用户缓存
        '''
        update_users_cache.delay([user.username])

    def add_users_to_group(self, users, group):
        '''
        更新用户缓存
        '''
        update_users_cache.delay([user.username for user in users])

    def sort_users_in_group(self, users, group):
        '''
        目前不影响缓存
        '''

    def add_user_to_groups(self, user, groups):
        '''
        更新用户缓存
        '''
        update_users_cache.delay([user.username])

    def delete_user_from_groups(self, user, groups):
        '''
        更新用户缓存
        '''
        update_users_cache.delay([user.username])

    def delete_users_from_group(self, users, group):
        '''
        更新用户缓存
        '''
        update_users_cache.delay([user.username for user in users])

    def add_dept_to_dept(self, dept, parent_dept):
        '''
        更新下属所有子孙部门及其成员
        '''
        self._move_node_to_node(dept, parent_dept)

    def sort_depts_in_dept(self, depts, parent_dept):
        '''
        目前不影响缓存
        '''

    def add_group_to_group(self, group, parent_group):
        '''
        更新下属所有子孙组及其成员
        '''
        self._move_node_to_node(group, parent_group)

    def sort_groups_in_group(self, groups, parent_group):
        '''
        目前不影响缓存
        '''

    def move_group_to_group(self, group, parent_group):
        '''
        更新下属所有子孙组及其成员
        '''
        self._move_node_to_node(group, parent_group)

    def move_dept_to_dept(self, dept, parent_dept):
        '''
        更新下属所有子孙部门及其成员
        '''
        self._move_node_to_node(dept, parent_dept)

    @staticmethod
    def _move_node_to_node(node, parent_node):    # pylint: disable=unused-argument
        '''
        更新下属所有子孙节点及其成员
        '''
        nodes = list(node.downstream)
        update_nodes_cache.delay([node.node_uid for node in nodes])

        user_uids = [item['user__username'] for item in \
            node.member_cls.valid_objects.filter(owner__in=nodes).values('user__username')]
        update_users_cache.delay(user_uids)
