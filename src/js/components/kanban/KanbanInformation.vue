<template>
    <div>
        <div class="container">
            <div class="card">
                <div class="card-body">
                    <h1>Kanban Information</h1>
                    <hr>
                    <div class="row">
                        <!-- Instructions -->
                        <div class="col-md-4">
                            <strong>Instructions</strong>
                            <p class="text-instructions">
                                To add a new card to the board - please click on "New Card". You can link a card to an
                                existing object like a project or task by clicking on "Link Existing Object".
                            </p>
                            <p class="text-instructions">
                                You can drag and drop cards.
                            </p>
                        </div>

                        <!-- Add cards -->
                        <div class="col-md-8">
                            <h2 v-html="kanbanBoardResults[0]['fields']['kanban_board_name']"></h2><br/>
                            <a class="kanban-link"
                               href="javascript:void(0)"
                               v-on:click="addNewKanbanCard"
                            >
                                New Card
                            </a><br/>
                            <a class="kanban-link"
                               href="javascript:void(0)"
                               v-on:click="addNewLink"
                            >
                                Link Existing Object
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <hr>

        <!-- Rendering the Kanban Container -->
        <kanban-board v-bind:column-results="columnResults"
                      v-bind:kanban-board-results="kanbanBoardResults"
                      v-bind:kanban-card-results="localKanbanCardResults"
                      v-bind:level-results="levelResults"
                      v-bind:new-card-info="newCardInfo"
                      v-on:double_clicked_card="doubleClickedCard($event)"
        ></kanban-board>

        <!-- MODALS -->
        <new-kanban-card v-bind:kanban-card-results="kanbanCardResults"
                         v-bind:column-results="columnResults"
                         v-bind:level-results="levelResults"
                         v-bind:kanban-board-results="kanbanBoardResults"
                         v-on:new_card="newCard($event)"
        ></new-kanban-card>

        <card-information v-bind:card-information="cardInformation"
                          v-on:update_card="updateCard($event)"
        ></card-information>

        <new-kanban-link-wizard v-bind:location-id="locationId"
                                v-bind:column-results="columnResults"
                                v-bind:level-results="levelResults"
                                v-on:new_card="newCard($event)"
        ></new-kanban-link-wizard>
    </div>
</template>

<script>
    import { Modal } from "bootstrap";

    export default {
        name: "KanbanInformation",
        props: {
            columnResults: Array,
            kanbanBoardResults: Array,
            kanbanCardResults: Array,
            levelResults: Array,
            locationId: Number,
        },
        data() {
            return {
                cardInformation: {},
                localKanbanCardResults: this.kanbanCardResults,
                newCardInfo: [],
            }
        },
        methods: {
            addNewKanbanCard: function() {
                var addKanbanCardModal = new Modal(document.getElementById('addKanbanCardModal'));
                addKanbanCardModal.show();
            },
            addNewLink: function() {
                var newLinkModal = new Modal(document.getElementById('newLinkModal'));
                newLinkModal.show();
            },
            doubleClickedCard: function(data) {
                //Update the cardInformationId with the card id
                this.cardInformation = data;
            },
            newCard: function(data) {
                this.newCardInfo = data;
            },
            updateCard: function(data) {
                console.log("GOT HERE!");
                //Loop through the results - when the id's match. Update the data.
                this.localKanbanCardResults.forEach(row => {
                    //Check to see if the primary keys match - if they do update the data
                    if (row['pk'] == data['kanban_card_id']) {
                        row['fields']['kanban_card_text'] = data['kanban_card_text'];
                    }
                }) 
            },
        }
    }
</script>

<style scoped>

</style>
