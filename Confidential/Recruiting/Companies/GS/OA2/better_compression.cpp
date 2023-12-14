string betterCompression(string s) {
   stringstream ss( s );
   map<char,int> M;
   char c;
   int n;
   while( ss >> c >> n ) M[c] += n;

   string result;
   for ( auto pr : M ) result += pr.first + to_string( pr.second );
   return result;
}