{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6a1ae3f5",
   "metadata": {},
   "outputs": [],
   "source": [
    "from wordpress_xmlrpc import Client, WordPressPost\n",
    "from wordpress_xmlrpc.methods.posts import GetPosts, NewPost\n",
    "from wordpress_xmlrpc.methods.users import GetUserInfo\n",
    "from wordpress_xmlrpc import Client, WordPressPost\n",
    "from wordpress_xmlrpc.compat import xmlrpc_client\n",
    "from wordpress_xmlrpc.methods import media, posts\n",
    "\n",
    "# WordPress credentials\n",
    "url = '' #Enter Your Wordpress url\n",
    "\n",
    "username = '' #Enter Your Wordpress username\n",
    "password = '' #Enter Your Wordpress password\n",
    "\n",
    "def make_post(content):\n",
    "    wp = Client('', # Enter Your Wordpress site info\n",
    "                username, password)\n",
    "    post = WordPressPost()\n",
    "    post.title = content['title']\n",
    "    post.content = content['body']\n",
    "    post.terms_names = {\n",
    "        'post_tag': [content['tags'], 'ContentBooster'],\n",
    "        'category': ['News', 'Update']\n",
    "    }\n",
    "    # Lets Now Check How To Upload Media Files\n",
    "    #filename = '1.jpg'\n",
    "    filename = content['filename']\n",
    "    data = {\n",
    "        'name': filename,\n",
    "        'type': 'image/jpeg'  # Media Type\n",
    "    }\n",
    "    # Now We Have To Read Image From Our Local Directory !\n",
    "    with open(filename, 'rb') as img:\n",
    "        data['bits'] = xmlrpc_client.Binary(img.read())\n",
    "        response = wp.call(media.UploadFile(data))\n",
    "    attachment_id = response['id']\n",
    "\n",
    "    # Above Code Just Uploads The Image To Our Gallery\n",
    "    # For Adding It In Our Main Post We Need To Save Attachment ID\n",
    "    post.thumbnail = attachment_id\n",
    "    post.post_status = 'pending'\n",
    "    post.id = wp.call(posts.NewPost(post))\n",
    "    # Set Default Status For Post .i.e Publish Default Is Draft\n",
    "\n",
    "    # We Are Done With This Part :) Lets Try To Run It\n",
    "    print(\"Sucessfully Posted To Our Blog !\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f831562f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sucessfully Posted To Our Blog !\n",
      "Sucessfully Posted To Our Blog !\n",
      "Sucessfully Posted To Our Blog !\n",
      "Sucessfully Posted To Our Blog !\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Read csv file\n",
    "content_generated_quora_data = pd.read_csv('Quora_Scraped_Data.csv')\n",
    "\n",
    "\n",
    "for index, row in content_generated_quora_data.iterrows():\n",
    "    try:\n",
    "        if pd.notna(row['OPEN_AI_Prompt']):\n",
    "            if pd.notna(row['Pic_File_Name']) and isinstance(row['Pic_File_Name'], str):\n",
    "            # Define content for the WordPress post\n",
    "                content = {\n",
    "                    'title': f\"<h4> {row['AI_Generated_Blog_Post_Title']}<h4>\",\n",
    "                    'body': f\"<div style='color: black; font-size: 12px;'>{row['AI_Generated_Blog_Post_Content']}</div>\",\n",
    "                    'tags': row['SearchTerm'],\n",
    "                    'filename': row['Pic_File_Name'],\n",
    "                }\n",
    "\n",
    "                make_post(content)\n",
    "        \n",
    "    except Exception as e:\n",
    "        print('Error: ' + str(e))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "950824a1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
