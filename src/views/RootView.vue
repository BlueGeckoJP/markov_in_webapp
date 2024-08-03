<script setup lang="ts">
import MessageBox from "@/components/MessageBox.vue";
import axios from "axios";
import { nextTick, ref, type Ref } from "vue";

let messages: Ref<Array<any>> = ref([]);

async function onClickSubmitButton() {
  await axios.get("/api").then((res) => {
    messages.value.push({ type: MessageBox, message: res.data });
  });
  await scrollToBottom();
}

async function scrollToBottom() {
  let messageContainer = document.getElementById("message-container");
  await nextTick();
  if (messageContainer) {
    messageContainer.scrollTo({
      top: messageContainer.scrollHeight,
      behavior: "smooth",
    });
  }
}
</script>

<template>
  <div id="top">
    <div id="message-container">
      <component
        v-for="(msg, index) in messages"
        :key="index"
        :is="msg.type"
        :message="msg.message"
      />
    </div>
    <div id="chatbox-container">
      <input id="chatbox" />
      <button id="submit-button" @click="onClickSubmitButton()">⬆</button>
    </div>
  </div>
</template>

<style>
#top {
  background-color: var(--f-color);
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

#message-container {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  width: 100%;
  height: calc(100% - 115px);
  overflow: auto;
}

#chatbox-container {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

#chatbox {
  margin: 20px;
  margin-right: 10px;
  width: 60%;
  height: 45px;
  border: none;
  outline: none;
  border-radius: 15px;
  background-color: var(--s-color);
  color: var(--t-color);
  padding: 10px;
  font-size: large;
  transition: all 0.3s ease;
  box-shadow: 0 0 4px var(--s-color);
}

#chatbox:focus {
  box-shadow: 0 0 4px var(--t-color);
}

#submit-button {
  margin: 20px;
  margin-left: 0;
  border: none;
  outline: none;
  border-radius: 15px;
  background-color: var(--s-color);
  color: var(--t-color);
  padding: 10px;
  font-size: large;
  transition: all 0.3s ease;
  box-shadow: 0 0 4px var(--s-color);
  height: 45px;
}

#submit-button:hover {
  box-shadow: 0 0 4px var(--t-color);
}
</style>
