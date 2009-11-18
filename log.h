/* avoid reinclusion of logging functions */
#ifndef LOGGING
#define LOGGING 

#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#define LOGFILE "run.log"
char logBuff[256]; /* default buffer for sprintf */

/*
This module is used the following way
main()
{
init_logging();
sprintf(logBuff,"pid= %d message=%s",24,"exiting..");
log_message(logBuff);
}
 */
FILE *logFile;

void log_message(char *message){
  // time_t curTime;
  //time(&curTime);
  fprintf(logFile,"%s\n", message);
  fflush(logFile);
  return;
}

void exit_logging(){
  log_message("stopping logging");
  fclose(logFile);
}
/*
setup logging for appending output to a file
*/
void init_logging(){
  logFile = fopen(LOGFILE,"a");
  if(atexit(exit_logging)){
    printf("failed to start logging\n");
    exit(1);
      }
  log_message("starting logging");
}

#endif
