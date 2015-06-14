class AuthRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'auth':
            return 'users'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'auth':
            return 'users'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'auth' or \
           obj2._meta.app_label == 'auth':
           return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        if app_label == 'auth':
            return db == 'users'
        return None


class AppEntryRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'app_entry':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'app_entry':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'app_entry' or \
           obj2._meta.app_label == 'app_entry':
           return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        if app_label == 'app_entry':
            return db == 'default'
        return None


class AppProfileRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'app_user':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'app_user':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'app_user' or \
           obj2._meta.app_label == 'app_user':
           return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        if app_label == 'app_user':
            return db == 'default'
        return None

