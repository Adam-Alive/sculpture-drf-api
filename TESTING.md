# Testing
 
> Return to the [README.md](README.md) file.
 
## Code Validation

### Python
 
I have used the [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all Python files.

There were no errors, apart from minor indentation and whitespace errors, all of which have been corrected. A sample test is shown here:




 ## Bugs
 
 - **Issue:** Favicon only showing on home page.
  
 - **Fix:** Research on Stack Overflow suggested I link to the favicon from the base.html using Django template language, rather than html, and this solved the problem:

    **Before:**

    **After:**

## Unfixed Bugs

Duplicate bookings.
