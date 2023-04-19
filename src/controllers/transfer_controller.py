"""Transfer controller"""""
from general.util import make_api_post_request
from general.headers import headers, base_url


class TransferController:
    """Transfer controller"""
    @staticmethod
    def create_transfer(current_acc_id: int, username_receiver: str, transfer_value: str, currency: str, description: str):
        """Create a new transfer"""
        endpoint_url = f"{base_url}/transfer/create_transfer/{current_acc_id}/{username_receiver}/{transfer_value}/{currency}/{description}"
        return make_api_post_request(endpoint_url, headers=headers)

    @staticmethod
    def delete_transfer_by_acc_id(account_id: int):
        """Delete a transfer"""
        # endpoint_url = f"{base_url}/transfer/delete_transfer_by_acc_id/{account_id}"
        # make_api_post_request(endpoint_url, headers=headers)
        # return True
        return "Not implemented yet"
