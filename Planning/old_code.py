    # if 'dl' in request.POST:
    #
    #     try:
    #
    #         csv_text = request.POST.get('csv_text')
    #         segmented_list = [[item.strip() for item in row.split(',')] for row in csv_text.split('\n')]
    #         response = HttpResponse(content_type = 'text/csv')
    #         response['Content-Disposition'] = 'attachment; filename = "export_data.csv"'
    #         writer = csv.writer(response)
    #         writer.writerow(segmented_list[0])
    #         writer.writerows(segmented_list[1:])
    #         return response
    #
    #     except:
    #
    #         context={
    #             'message': 'Something went wrong'
    #         }
    #         return render(request, template_name, context)
    #
    # elif 'package' in request.POST:
    #
    #     key = generate_key(10)
    #     csv_text = request.POST.get('csv_text')
    #     segmented_list = [[item.strip() for item in row.split(',')] for row in csv_text.split('\n')]
    #     file_name = key + ".csv"
    #
    #     with open(file_name,'w') as f:
    #
    #         writer = csv.writer(f)
    #         writer.writerow(segmented_list[0])
    #         writer.writerows(segmented_list[1:])
    #
    #     file_name = default_storage.save(file_name, open(file_name))
    #     temp = TemporaryFile(key = key, data = file_name)
    #     temp.save()
    #     context={
    #         'message': 'Saved! \n Here is your key: ' + key
    #     }
    #     return render(request, template_name, context)
