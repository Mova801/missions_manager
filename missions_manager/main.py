from core.client import controller


def main() -> None:
    """
    Main entry in client application.
    :return: None
    """
    app = controller.ClientController()
    app.run()


if __name__ == '__main__':
    main()
