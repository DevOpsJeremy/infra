from os.path import join
from os.path import normpath
from ansible.config.manager import ConfigManager

cm = ConfigManager()


def collection_to_path(
    collection_name: str,
    collections_path: str = normpath(
        join(cm.get_config_value("ANSIBLE_HOME"), "collections")
    ),
) -> str:
    """
    Convert a collection name to its filesystem path.

    :param collection_name: Name of the collection in the format 'namespace.collection'.
    :param collections_path: Base path where collections are stored.
    :return: Full filesystem path to the collection.
    """

    namespace, name = collection_name.split(".")
    collection_path = join(collections_path, "ansible_collections", namespace, name)
    return normpath(collection_path)


class FilterModule(object):
    def filters(self):
        return {
            "collection_to_path": collection_to_path,
        }
