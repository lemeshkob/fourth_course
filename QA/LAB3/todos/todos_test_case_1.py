import todos_setup
import todos_actions

if __name__ == "__main__":
    """
    TestCase trying to add ne element, edit it and mark it as checked
    """
    driver = todos_setup.setUp()
    driver.get('http://todomvc.com/examples/angularjs/#/')
    todos_actions.add_new_element(driver, 'Hello there!')
    todos_actions.perform_edit(driver, "BRUH")
    todos_actions.perform_done(driver)