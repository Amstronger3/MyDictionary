<template>
  <div>
    <AddWordModal />

    <div style="display: flex; justify-content: center">
      <v-card>
        <v-card-title>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
        </v-card-title>

        <v-data-table
          @click:row="selectWord"
          style="width: 600px"
          :headers="headers"
          :items="words"
          :item-class="backgroundRow"
          item-key="id"
          :search="search"
          dense
        >
          <template v-slot:[`item.original_word`]="{ item }">
            <div v-if="selectedWord.id === item.id && editMode">
              <v-text-field
                dense
                hide-details
                v-model="selectedWord.original_word"
              ></v-text-field>
            </div>
            <span v-else>{{ item.original_word }}</span>
          </template>

          <template v-slot:[`item.translate_original_word`]="{ item }">
            <div v-if="selectedWord.id === item.id && editMode">
              <v-text-field
                dense
                hide-details
                v-model="selectedWord.translate_original_word"
              ></v-text-field>
            </div>
            <span v-else>{{ item.translate_original_word }}</span>
          </template>
        </v-data-table>
      </v-card>

      <div class="ma-2" style="display: block">
        <div>
          <v-btn width="90" color="success" @click="addWord" v-show="!editMode">
            Add
          </v-btn>
        </div>
        <div class="mt-2">
          <v-btn width="90" color="info" @click="editWord" v-show="!editMode"
            >Edit</v-btn
          >
        </div>
        <div class="mt-2" v-show="!editMode">
          <v-btn width="90" color="error" @click="deleteWord">Delete</v-btn>
        </div>
        <div class="mt-2" v-show="editMode">
          <v-btn width="90" color="success" @click="saveEditableWord"
            >Save</v-btn
          >
        </div>
        <div class="mt-2" v-show="editMode">
          <v-btn width="90" color="error" @click="cancelEditWord">Cancel</v-btn>
        </div>
      </div>
    </div>

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
    <v-alert
      style="position: absolute; top: 30px; left: 30px"
      dense
      type="warning"
      :value="alert"
      max-width="300"
      >{{ alertMessage }}</v-alert
    >
  </div>
</template>

<script>
import axios from "axios";
import { eventBus } from "../main";
import AddWordModal from "../components/AddWordModal.vue";

export default {
  components: {
    AddWordModal,
  },
  name: "Home",
  data() {
    return {
      alertMessage: "",
      alert: false,
      successSnackbar: false,
      timeoutSnackbar: 1000,
      search: "",
      editMode: false,
      selectedWord: {},
      words: [],
      headers: [
        { text: "Original word", value: "original_word", width: "300" },
        { text: "Translate", value: "translate_original_word", width: "300" },
      ],
    };
  },

  mounted() {
    this.getWords();
  },

  methods: {
    cancelEditWord() {
      this.editMode = false;
      this.getWords();
    },

    deleteWord() {
      if (!Object.keys(this.selectedWord).length) {
        this.alert = true;
        this.alertMessage = "Please, select word!";
        setTimeout(() => {
          this.alert = false;
        }, 2000);
        return;
      }

      axios
        .delete(`/api/v1/words/${this.selectedWord.id}/`)
        .then((resp) => {
          this.successSnackbar = true;
          this.selectedWord = {};
          this.editMode = false;
          this.getWords();
        })
        .catch((error) => console.log(error));
    },

    saveEditableWord() {
      axios
        .put(`/api/v1/words/${this.selectedWord.id}/`, {
          original_word: this.selectedWord.original_word,
          translate_original_word: this.selectedWord.translate_original_word,
        })
        .then((resp) => {
          this.successSnackbar = true;
          this.selectedWord = {};
          this.editMode = false;
          this.getWords();
        })
        .catch((error) => console.log(error));
    },

    editWord() {
      if (!Object.keys(this.selectedWord).length) {
        this.alert = true;
        this.alertMessage = "Please, select word!";
        setTimeout(() => {
          this.alert = false;
        }, 2000);
        return;
      }

      this.editMode = true;
    },

    backgroundRow(item) {
      return item.id === this.selectedWord.id ? "blue lighten-4" : "";
    },

    selectWord(item) {
      this.selectedWord = item;
    },

    getUpdatedWords(data) {
      console.log(data);
    },

    addWord() {
      eventBus.$emit("showModalAddWord");
    },

    getWords() {
      axios
        .get("/api/v1/words/")
        .then((resp) => {
          this.words = resp.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    eventBus.$on("updatedWords", this.getWords);
  },
};
</script>
