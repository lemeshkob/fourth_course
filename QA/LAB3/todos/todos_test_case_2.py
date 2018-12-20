import todos_actions
import todos_setup

if __name__ == '__main__':
    driver = todos_setup.setUp()
    driver.get('http://todomvc.com/examples/angularjs/#/')
    todos_actions.add_new_element(driver, 'Hello there!')
    todos_actions.perform_done(driver)
    todos_actions.perform_clear_completed(driver)