from essential_imports import *
from inline_handlers.json_handlers import *
from inline_handlers.places_inline import *
from inline_handlers.budget_inline import *
from inline_handlers.final_inline import *
from inline_handlers.more_filters_inliners import *
from inline_handlers.generating_list import *
from inline_handlers.commands_and_triggers import*


app = Flask(__name__)


@app.route('/', methods=['POST','GET'])

def index():
    if request.method == 'POST':

        main()
        msg = request.get_json()
        write_json(msg, 'telegram_request.json')
        return Response('ok', status=200)

    else:
        return '<h1>cafe-decider-ngp</h1>'

#* MAIN FUNCTION
def main():
    
    application = Application.builder().token(TOKEN).build()


    conversation_handler = ConversationHandler(
        entry_points=[MessageHandler(filters=filters.Regex("^(Hey|hey|hi|Hi|HI|HEY)$"), callback=start_conversation)],
        states={
            START : [
                CallbackQueryHandler(budget, pattern="^(budget)$"),
                CallbackQueryHandler(display_types_for_types, pattern="^(place)$"),       
            ],
            BUDGET : [
                CallbackQueryHandler(display_types, pattern="^(100-150|150-300|300-600|600-1000+)$"),
                CallbackQueryHandler(generate_list, pattern="^(Beverages|Clubs|Pubs|Lounge|Roadside|MainCourse|KhauGallis|Cafe|South Indian Exclusives)$"),           
            ],
            TYPE :[
                CallbackQueryHandler(display_more_filters, pattern="^(MainCourse|Cafe)$"),
                CallbackQueryHandler(generate_list_filters, pattern="^(None|Pure Veg|Serves Alcohol|KhauGallis|South Indian Exclusives|Clubs|Pubs|Lounge|Beverages)$"),
                
                ],
            END : [CallbackQueryHandler(deploy_results, pattern="^"+str(END)+"$"),]
        },
        fallbacks=[
            # MessageHandler(filters=filters.Regex("^(STOP|Stop|stop|abort|ABORT|abort)$"), callback=end_conversation),
            CommandHandler(command='troubleshoot', callback=troubleshoot_command)
        ]
    )
    application.add_handlers(
        [
            CommandHandler("start", start_command),
            conversation_handler,
        ]
    )
    application.run_polling()


if __name__ == "__main__":
    main()