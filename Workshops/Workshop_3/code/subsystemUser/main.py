from loggingSystem.loging import Logger
from subsystemUser.proxyUser import ProxyUser
from subsystemCatalog.catalog import Catalog
from subsystemUser.authentication import User
from subsystemUser.authentication import Admin


def main():
    authentication = authentication()
    catalog = Catalog()
    logger = Logger()

    admin = Admin("Admin", "admin@example.com", "password") #Se inicializa los atributos que debe de ingresar el administrador
    user = User("User", "user@example.com", "password") #Se inicializa ls atributos que va a ingresar el usuario

    authentication.register_user(admin)
    authentication.register_user(user)

    proxy_admin = ProxyUser(catalog, admin)  
    proxy_user = ProxyUser(catalog, user)

    while True:
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            email = input("Enter email: ")
            password = input("Enter password: ")
            user = authentication.authenticate_user(email, password)
            if user:
                print(f"Welcome, {user.name}!")
                if user.rol == "Admin":
                    proxy = proxy_admin
                else:
                    proxy = proxy_user
                while True:
                    print("1. Add vehicle")
                    print("2. Delete vehicle")
                    print("3. Update vehicle")
                    print("4. Search vehicles")
                    print("5. Logout")
                    choice = input("Choose an option: ")

                    if choice == "1":
                        # Add vehicle logic here
                        pass
                    elif choice == "2":
                        # Delete vehicle logic here
                        pass
                    elif choice == "3":
                        # Update vehicle logic here
                        pass
                    elif choice == "4":
                        query = input("Enter search query: ")
                        result =proxy.search_vehicles(query)
                        for vehicle in result:
                            print(vehicle)
                        print("Search cache:")
                        for i, cache in enumerate(proxy.catalog.search_cache):
                            print(f"{i + 1}. {len(cache)} results")
                    elif choice == "5":
                        break
            else:
                print("Invalid email or password")
        elif choice == "2":
            # Register user logic here
            pass
        elif choice == "3":
            break

if __name__ == "__main__":
    main()