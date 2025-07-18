using System;
using TMPro;
using UnityEngine;

public class UI : MonoBehaviour
{
    [SerializeField]
    TextMeshProUGUI chatResponseText;

    [SerializeField]
    TMP_InputField contentInput;

    public void CreateManagerButton()
    {
        var request = new JsonStructures.ChatInitRequest
        {
            context = contentInput.text
        };


        HttpWrap.SendPostRequest("/chat/init", request).ContinueWith(task =>
        {
            if (task.IsCompletedSuccessfully)
            {
                JsonStructures.ChatInitResponse response = 
                    JsonUtility.FromJson<JsonStructures.ChatInitResponse>(task.Result);

                chatResponseText.text = "Chat ID: " + response.chatId;  
            }
            else
            {
                Debug.LogError("Error: " + task.Exception);
            }
        });
    }
    
}
