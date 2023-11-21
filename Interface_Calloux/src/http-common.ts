import axios from "axios";
import type { AxiosInstance } from "axios";
import URL from "@/ApiAxios";

let apiClient: AxiosInstance = axios.create({
    baseURL: URL+":8888/api",
    headers: {
        "Content-type": "application/json",
        "Authorization": "Bearer " + localStorage.getItem('access'),
    },
});

export function refresh(token: String){
    return axios.create({
        baseURL: URL+":8888/api",
        headers: {
            "Content-type": "application/json",
            "Authorization": "Bearer " + token,
        },
    });
}

export default apiClient;
