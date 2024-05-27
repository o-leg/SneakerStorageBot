class RequestBodyFormulator:
    @staticmethod
    def form_by_article(article: str) -> dict:
        """
        Forms a request body based on article SKU.

        Parameters:
            article (str): The article SKU.

        Returns:
            dict: The request body.
        """
        return {'sku': article}

    @staticmethod
    def form_by_name(name: str, limit: int = 0) -> dict:
        """
        Forms a request body based on name.

        Parameters:
            name (str): The name to search.
            limit (int): Limit the number of results.

        Returns:
            dict: The request body.
        """
        body = {'search': name}
        if limit:
            body['limit'] = limit
        return body
