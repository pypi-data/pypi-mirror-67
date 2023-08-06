This python library and script are used to help manage a set of subuid/subgid
files for kernel user namespaces.  Currently they are expect these to be
managed by hand and users in the name service switch do not automatically get
added (and if you manage your users with a network based SSSD configuration
this becomes even more challenging).

When you are mapped a range of uids in a user name space they can not overlap
with any other users.  So in a multi-tenant system this can be a challenge if
you have a lot of different users to make sure that these bands don't overlap.

The script `addsub` provides a simple way to add a user to a given file and
keep the bands of uids discrete.  The default is that if no users are already
in the file the largest 32bit integer rounded (4294000000) will be used along
with an allocation of 100000 uids.  We will not automatically allocate a
starting uid < 100000.
