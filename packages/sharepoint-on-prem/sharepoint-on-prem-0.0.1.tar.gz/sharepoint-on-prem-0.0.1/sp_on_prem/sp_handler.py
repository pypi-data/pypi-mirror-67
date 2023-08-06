import os
import json
from requests import Session, Response
from requests_ntlm2 import HttpNtlmAuth


class SPFileHandler(Session):
    __HEADERS = {"Accept": r"application/json;odata=verbose"}
    __CONTEXT_ENDPOINT = r"_api/contextinfo"

    def __init__(self, site_root_url: str, username: str, password: str):
        super().__init__()
        ## TODO: Add a regex check setter function
        self.site_url = site_root_url
        self.auth = HttpNtlmAuth(
            username=username,
            password=password
        )

    @property
    def form_request_digest(self) -> dict:
        """
        Get request_digest for POST requests.
        :return: request_digest
        """
        context_url = f"{self.site_url}/{self.__CONTEXT_ENDPOINT}"
        r_context = self.post(url=context_url, headers=self.__HEADERS, verify=False)
        ## TODO: Add a checker
        form_request_digest = json.loads(r_context.content)["d"]["GetContextWebInformation"]["FormDigestValue"]
        return form_request_digest

    def _return_response_or_error_code(self, r: Response) -> Response:
        """
        A helper function that checks if the connection to SharePoint is successful.
        :param r: response from the request
        :return: the response
        """
        if r.status_code == 200:
            return r
        else:
            raise ConnectionError(r.status_code)

    def _get_file_content(self, rf: str, file_name: str) -> Response:
        """
        a helper function that reads the content of the file in SharePoint.
        :param rf: the remote folder (or library) name in SharePoint
        :param file_name: the file name
        :return: file content
        """
        url = f"{self.site_url}_api/web/GetFolderByServerRelativeUrl('{rf}')/Files('{file_name}')/$value"
        r = self.get(url=url, headers=self.__HEADERS, verify=False)
        return self._return_response_or_error_code(r)

    def get_file_list(self, rf: str) -> list:
        """
        Get a list of files in the SharePoint Folder
        :param rf: the remote folder (or library) name in SharePoint
        :return: the file list of the SharePoint folder
        """
        url = f"{self.site_url}_api/web/GetFolderByServerRelativeUrl('{rf}')/files?$expand=ListItemAllFields"
        r = self.get(url=url, headers=self.__HEADERS, verify=False)
        r_verified = self._return_response_or_error_code(r)
        file_list = [json.loads(r_verified.content)['d']['results'][i] for i in
                     range(len(json.loads(r.content)['d']['results']))]

        return file_list

    def download_file(self, rf: str, lf: str, file_name: str) -> Response:
        """
        The method for downloading file from SharePoint.
        :param rf: the remote folder (or library) name in SharePoint
        :param lf: the local folder name
        :param file_name: the file name
        :return: status of downloading
        """
        file_content = self._get_file_content(rf=rf, file_name=file_name).content
        with open(os.path.join(lf, file_name), "wb") as f:
            f.write(file_content)
        return file_content

    def upload_file(self, rf: str, lf: str, file_name: str, overwrite: bool = False) -> Response:
        """
        The method for uploading file to SharePoint.
        :param rf: the remote folder (or library) name in SharePoint
        :param lf: the local folder name
        :param file_name: the file name
        :return: status of uploading
        """
        url = f"{self.site_url}_api/web/GetFolderByServerRelativeUrl('{rf}')/Files/add(url='{file_name}',overwrite={'true' if overwrite else 'false'})"
        headers = {**self.__HEADERS, "X-RequestDigest": self.form_request_digest}
        with open(os.path.join(lf, file_name), "rb") as f:
            body = f.read()
        r = self.post(url=url, headers=headers, data=body, verify=False)
        return self._return_response_or_error_code(r)

    def delete_file(self, rf: str, file_name: str) -> Response:
        """
        The method for deleting file in SharePoint.
        :param rf: the remote folder (or library) name in SharePoint
        :param file_name: the file name
        :return: status of deleting
        """
        url = f"{self.site_url}_api/web/GetFolderByServerRelativeUrl('{rf}/{file_name}')"
        headers = {
            **self.__HEADERS,
            "X-RequestDigest": self.form_request_digest,
            "X-HTTP-Method": "DELETE"
        }
        r = self.post(url=url, headers=headers, verify=False)
        return self._return_response_or_error_code(r)
