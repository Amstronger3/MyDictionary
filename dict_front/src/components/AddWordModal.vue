<template>
  <v-dialog persistent width="600" v-model="dialog">
    <v-card>
      <div style="display: flex">
        <v-card-title>
          <span>Add word to your dictionary</span>
        </v-card-title>
        <v-spacer></v-spacer>
        <v-btn text fab small @click="closeModal"
          ><v-icon>mdi-close</v-icon></v-btn
        >
      </div>

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

      <v-snackbar
        min-height="30"
        min-width="150"
        color="success"
        v-model="successSnackbar"
        :timeout="timeoutSnackbar"
        top
        right
      >
        <div style="display: flex; justify-content: center">
          <b>Success!</b>
        </div>
      </v-snackbar>
    </v-card>
    <v-alert
      style="position: absolute; top: 30px; left: 30px"
      dense
      type="warning"
      :value="alert"
      max-width="300"
      >{{ alertMessage }}</v-alert
    >
  </v-dialog>
</template>

<script>
import axios from "axios";
import { eventBus } from "../main";
export default {
  data() {
    return {
      alertMessage: "",
      alert: false,
      successSnackbar: false,
      timeoutSnackbar: 1000,
      orinalWord: "",
      translatedWord: "",
      dialog: false,
    };
  },
  methods: {
    closeModal() {
      this.dialog = false;
      this.orinalWord = "";
      this.translatedWord = "";
    },
    saveWord() {
      if (!this.orinalWord || !this.translatedWord) {
        this.alert = true;
        this.alertMessage = "Please, enter words!";
        setTimeout(() => {
          this.alert = false;
        }, 2000);
        return;
      }

      axios
        .post("/api/v1/words/", {
          original_word: this.orinalWord,
          translate_original_word: this.translatedWord,
        })
        .then((resp) => {
          eventBus.$emit("updatedWords");
          this.successSnackbar = true;
          this.orinalWord = "";
          this.translatedWord = "";
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