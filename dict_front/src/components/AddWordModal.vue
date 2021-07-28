<template>
  <v-dialog width="600" v-model="dialog">
    <v-card>
      <v-card-title> Add word to your dictionary </v-card-title>
      <v-card-text>
        <div style="display: flex; justify-content: center">
          <div>
            <v-text-field
              v-model="orinalWord"
              label="Original word"
              clearable
              hide-details
              outlined
              dense
            >
            </v-text-field>
          </div>

          <div>
            <v-text-field
              v-model="translatedWord"
              class="ml-2"
              label="Translate"
              clearable
              hide-details
              outlined
              dense
            >
            </v-text-field>
          </div>
        </div>
      </v-card-text>
      <v-card-actions>
        <v-btn color="success" @click="saveWord">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from "axios";
import { eventBus } from "../main";
export default {
  data() {
    return {
      orinalWord: "",
      translatedWord: "",
      dialog: false,
    };
  },
  methods: {
    saveWord() {
      if (!this.orinalWord || !this.translatedWord) {
        alert("Please, entry words!");
        return;
      }

      axios
        .post("/api/v1/words/", {
          original_word: this.orinalWord,
          translate_original_word: this.translatedWord,
        })
        .then((resp) => {
          eventBus.$emit("updatedWords");
        })
        .catch((error) => console.log(error));
    },

    showModal() {
      this.dialog = true;
    },
  },
  created() {
    eventBus.$on("showModalAddWord", this.showModal);
  },
};
</script>