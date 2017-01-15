#include <stdlib.h>
#include <stdio.h> 
#include <string.h>
int max_line_len = 1024;
char* readline(FILE *input);
const int nP = 10;
void getparameters(char* params[nP])
{
    FILE *fp;
    int index;
    //args_svm_classify_multiclass.txt
    //args_svm_learn_multiclass.txt
    fp=fopen("settings.txt","r");
    if(fp==NULL)
	{
		fprintf(stderr,"can't open file dataset information file\n");
		exit(1);
	}
    
    char *ptr;

    int i =0;
    char * line;
	while((line=readline(fp))!=NULL)
	{		
        if(line[0]=='/')
            continue; 
        params[i] = line; i++;
	}
    fclose(fp);
}
char* readline(FILE *input)
{
	int len;
	char *line = (char*)malloc(200 * sizeof(char));
	if(fgets(line,max_line_len,input) == NULL)
		return NULL;

	while(strrchr(line,'\n') == NULL)
	{
		max_line_len *= 2;
		line = (char *) realloc(line, max_line_len);
		len = (int) strlen(line);
		if(fgets(line+len,max_line_len-len,input) == NULL)
			break;
	}
	len = (int)strlen(line);
	if(len>0)
	{
		if(line[len-1]=='\n')
			line[len-1] ='\0';
	}
	return line;
}
