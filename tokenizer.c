#include <stdio.h>

int main(void)
{
   const char line[80] ;
   const char *ptr = line;
   char field [ 32 ];
   fgets(line,80,stdin);
   int n=0;
   while ( sscanf(ptr, "%s%n", field, &n) == 1 && (line[n]!='\0')  )
   {
      printf("field = \"%s\"\n", field);
      ptr += n; /* advance the pointer by the number of characters read */
      if(*ptr =='\0' || *ptr == '\n' )
         break;
   }
   return 0;
}


/*
sample output
C:\Users\Magical\Documents>stringparse.exe
my name is     vishal                   patel.
field = "my"
field = "name"
field = "is"
field = "vishal"
field = "patel."

PS: yes i programmed in Vista usign dev c++ :)
*/