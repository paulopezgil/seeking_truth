using System;
using System.Collections;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;
using UnityEngine;
using System.Text;

public static class HttpWrap
{
    const string base_url = "http://localhost:8000";

    private static readonly HttpClient client = new HttpClient();

    public static async Task<string> SendGetRequest(string url)
    {
        string ret;
        ret = await client.GetStringAsync(base_url + url);

        return ret;
    }

    public static async Task<string> SendPostRequest(string url, object content)
    {
        string json = JsonUtility.ToJson(content);
        Debug.Log(json);
        var stringContent = new StringContent(json, Encoding.UTF8, "application/json");
        var response = await client.PostAsync(base_url + url, stringContent);
        response.EnsureSuccessStatusCode();
        return await response.Content.ReadAsStringAsync();
    }
}
